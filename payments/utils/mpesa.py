import base64
import math
import time
from datetime import datetime

import requests
from phonenumber_field.phonenumber import PhoneNumber
from requests.auth import HTTPBasicAuth
from rest_framework import serializers
from rest_framework.response import Response

from constants.models import Constant
from mobile.models import Mobile
from payments.models import Transaction
from school.models import School
from student.models import Student


class Decorators:
    @staticmethod
    def refresh_token(decorated):
        def wrapper(gateway, *args, **kwargs):
            if (
                    gateway.access_token_expiration
                    and time.time() > gateway.access_token_expiration
            ):
                token = gateway.get_access_token()
                gateway.access_token = token
            return decorated(gateway, *args, **kwargs)

        return wrapper


class MpesaGateway:
    shortcode = None
    consumer_key = None
    consumer_secret = None
    access_token_url = None
    access_token = None
    access_token_expiration = None
    checkout_url = None
    timestamp = None

    def __init__(self):
        self.headers = None
        self.access_token_expiration = None
        self.shortcode = "4083027"
        self.consumer_key = "uQH9B9rRvYHvpM2ICYyvBdwR0UE6Pvz4"
        self.passkey ="9cd4dd3777a83ffc18c70766a77e1f2077dbaea17188f98235158ed533f3331d"
        self.consumer_secret = "DurpnNk6Z21uDjaW"
        self.password = self.generate_password()
        self.c2b_callback = "https://tafatalk.co.ke/api/v1/payments/callback"
        self.access_token_url = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        self.checkout_url = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        try:
            self.access_token = self.get_access_token()
            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            pass
        else:
            self.access_token_expiration = time.time() + 3400


    def generate_password(self):
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        print(f"TIME IS {self.timestamp} and self.shortcode is {self.shortcode}")
        password = self.shortcode + self.passkey + self.timestamp
        password_byte = password.encode("ascii")
        return base64.b64encode(password_byte).decode("utf-8")


    def getStudent(self):
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        print(f"TIME IS {self.timestamp} and self.shortcode is {self.shortcode}")
        password = self.shortcode + self.passkey + self.timestamp
        password_byte = password.encode("ascii")
        return base64.b64encode(password_byte).decode("utf-8")

    def get_access_token(self):
        try:
            res = requests.get(self.access_token_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        except Exception as e:
            raise e

        token = res.json()['access_token']
        self.headers = {"Authorization": "Bearer %s" % token}
        return token

    @Decorators.refresh_token
    def stk_push_request(self, amount, mobile, studentid, user, purpose, timestamp):
        student = None
        try:
            student = Student.objects.get(id=studentid)
        except Student.DoesNotExist:
            raise serializers.ValidationError(f"Student with the  ID {studentid}  does not exist")

        body = {
            "BusinessShortCode": self.shortcode,
            "Password": self.password,
            "Timestamp": self.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": math.ceil(float(amount)),
            "PartyA": mobile,
            "PartyB": self.shortcode,
            "PhoneNumber": mobile,
            "CallBackURL": self.c2b_callback,
            "AccountReference": str(mobile),
            "TransactionDesc": str(mobile),
            "headers": self.headers
        }

        try:
            print("HERE 0")
            res = requests.post(self.checkout_url, json=body, headers=self.headers, timeout=30)
            res_data = res.json()
            print("HERE 1    " + str(res_data))

            if res.ok:
                student = None
                if  Student.objects.get(id = studentid):
                    student = Student.objects.get(id = studentid)

                transaction = Transaction.objects.create(
                    mobile = mobile,
                    user = user,
                    amount = amount,
                    studentid = studentid,
                    student = student,
                    purpose = purpose,
                    checkoutid=res_data["CheckoutRequestID"],
                    timestamp=timestamp
                )
                transaction.save()

                data = {}

                data['details'] = "Registration was successful"
                return Response(data)

            else:
                print("HERE 2    " + str(res_data))
                raise Exception(f"{str(res_data['errorMessage'])}")
        except Exception as e:
            raise Exception(e)




    @staticmethod
    def check_status(data):
        try:
            status = data["Body"]["stkCallback"]["ResultCode"]
        except Exception as e:
            status = 1
        return status

    @staticmethod
    def getTransactionObjectWithSimilarCheckoutRequestId(data):
        checkout_request_id = data["Body"]["stkCallback"]["CheckoutRequestID"]
        transaction, _ = Transaction.objects.get_or_create(checkoutid=checkout_request_id)
        return transaction



    def callback(self, data):
        status = self.check_status(data)
        transaction = self.getTransactionObjectWithSimilarCheckoutRequestId(data)

        if not transaction:
            checkout_request_id = data["Body"]["stkCallback"]["CheckoutRequestID"]
            raise Exception(f"Transaction with reference Id {checkout_request_id} not found!")

        amount = 0
        phone_number = 0
        receiptnumber = 0
        if status == 0:
            items = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"]
            for item in items:
                if item["Name"] == "Amount":
                    amount = item["Value"]
                elif item["Name"] == "MpesaReceiptNumber":
                    receiptnumber = item["Value"]
                elif item["Name"] == "PhoneNumber":
                    phone_number = item["Value"]

            if  transaction.purpose == "TOKEN":
                student = transaction.student
                student.active = True
                student.activefromdate = transaction.date_created.date()

                # ADD TOKENS AND MINUTES TO STUDENT
                userpaid = amount
                minutespershilling = Constant.objects.get(school=student.school).minutepershilling
                minutespertokenOrequivalentminutes = Constant.objects.get(school=student.school).minutespertokenOrequivalentminutes
                minutespertokenOrequivalentminutes = Constant.objects.get(school=student.school).minutespertokenOrequivalentminutes
                shillingspertokenOrequivalentshillings = Constant.objects.get(school=student.school).shillingspertokenOrequivalentshillings
                # SUBTRACT TOKENS AND MINUTES FROM USER

                student.tokenbalance = student.tokenbalance + (userpaid / shillingspertokenOrequivalentshillings)
                print(f"Student token balance is {student.tokenbalance} and userpaid {userpaid}  and shillings per token is {shillingspertokenOrequivalentshillings} so new token is {student.tokenbalance + (userpaid / shillingspertokenOrequivalentshillings)}")
                student = transaction.student
                student.save()

                school = student.school

                listOfMobiles = Mobile.objects.filter(school = school)
                numberOfPhones = len(listOfMobiles)
                shillingsPaidPerMobile = userpaid / numberOfPhones
                tokensToBeDeductedPerMobile = shillingsPaidPerMobile / shillingspertokenOrequivalentshillings

                for mobile in listOfMobiles:
                    mobile.standingtoken -= tokensToBeDeductedPerMobile
                    mobile.standingminutes -= (shillingsPaidPerMobile * minutespershilling)
                    mobile.save()
                    print(f"ALSO FOUND {student.fullname} - {school.name} - {mobile}")

            elif transaction.purpose == "REGISTRATION":
                student = transaction.student
                student.active = True
                student.activefromdate = transaction.date_created.date()
                student.save()
                pass

            user =  transaction.user
            if user:
                user.is_active = True
                user.save()

            transaction.amount = amount
            transaction.reference = receiptnumber
            transaction.mobile = PhoneNumber(raw_input=phone_number)
            transaction.receiptnumber = receiptnumber
            transaction.status = "COMPLETE"


        elif status == 1032:
            transaction.status = "CANCELLED"
        else:
            transaction.status = "FAILED"


        transaction.save()
        return True