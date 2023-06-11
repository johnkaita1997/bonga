from django.db.models import Sum

from constants.models import Constant
from mobile.models import Mobile


def transform_phone_number(phone_number):
    phonenumber = str(phone_number)
    print(f"Trying ", phonenumber)
    if not phonenumber:
        return phonenumber
    if phonenumber == "":
        return phonenumber
    if phonenumber.startswith('0'):
        print("It starts with zero")
        return '254' + phonenumber[1:]
    elif phonenumber.startswith('+254'):
        return phonenumber[1:]
    else:
        return phonenumber




def globalSchoolUnusedTokens():
    schooldevices = Mobile.objects.all()
    sum_standingtoken = schooldevices.aggregate(total_standingtoken=Sum('standingtoken'))['total_standingtoken']
    unusedtokens = sum_standingtoken
    sum_tokensconsumed = schooldevices.aggregate(total_tokensconsumed=Sum('tokensconsumed'))['total_tokensconsumed']
    tokensconsumed = sum_tokensconsumed
    return  sum_standingtoken

def globalSchoolUsedTokens():
    schooldevices = Mobile.objects.all()
    sum_tokensconsumed = schooldevices.aggregate(total_tokensconsumed=Sum('tokensconsumed'))['total_tokensconsumed']
    tokensconsumed = sum_tokensconsumed
    return  tokensconsumed




def specificSchoolUnusedTokens(schoolid):
    schooldevices = Mobile.objects.filter(school_id=schoolid)
    sum_standingtoken = schooldevices.aggregate(total_standingtoken=Sum('standingtoken'))['total_standingtoken']
    unusedtokens = sum_standingtoken
    sum_tokensconsumed = schooldevices.aggregate(total_tokensconsumed=Sum('tokensconsumed'))['total_tokensconsumed']
    tokensconsumed = sum_tokensconsumed
    return  sum_standingtoken

def specificSchoolUsedTokens(schoolid):
    schooldevices = Mobile.objects.filter(school_id=schoolid)
    sum_tokensconsumed = schooldevices.aggregate(total_tokensconsumed=Sum('tokensconsumed'))['total_tokensconsumed']
    tokensconsumed = sum_tokensconsumed
    return  tokensconsumed

def isEnoughToken(schoolid, amount):
    constant = Constant.objects.get(school_id=schoolid)
    shillingspertokenOrequivalentshillings = constant.shillingspertokenOrequivalentshillings
    tokensBeingBought = amount / shillingspertokenOrequivalentshillings

    tokensLeft = specificSchoolUsedTokens(schoolid)
    if tokensBeingBought > tokensLeft:
        return False
    else:
        return True


def myTokens(schoolid, amount):
    constant = Constant.objects.get(school_id=schoolid)
    shillingspertokenOrequivalentshillings = constant.shillingspertokenOrequivalentshillings
    tokensBeingBought = amount / shillingspertokenOrequivalentshillings
    tokensLeft = specificSchoolUsedTokens(schoolid)
    return print(f"Checkiing {tokensBeingBought} against {tokensLeft}")
