from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from appuser.models import AppUser
from payments.api.serializers import MpesaCheckoutSerializer
from payments.models import Transaction
from payments.utils import mpesa

gateway = mpesa.MpesaGateway()


class MpesaCallBackView(APIView):

    @csrf_exempt
    def post(self, request):
        data = request.data
        respose = gateway.callback(data)
        if respose:
            return Response({"details": "Success"}, status=status.HTTP_200_OK)
        return Response({"details": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MpesaCheckoutSerializer

class MpesaCheckoutView(generics.CreateAPIView):

    serializer_class = MpesaCheckoutSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            try:
                self.perform_create(serializer)
            except Exception as exception:
                return Response({"details": exception}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"details": "Success: An Mpesa request has been sent to your mobile."}, status=status.HTTP_201_CREATED)

        else:
            errors = serializer.errors
            return Response({"details": errors}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        mobile = serializer.validated_data['mobile']
        studentid = serializer.validated_data['studentid']
        amount = serializer.validated_data['amount']
        purpose = serializer.validated_data['purpose']
        timestamp = serializer.validated_data['timestamp']

        loggedinuser = self.request.user.id
        user = AppUser.objects.get(id=loggedinuser)
        serializer.validated_data['user'] = user

        gateway.stk_push_request(amount, mobile, studentid, user, purpose, timestamp)



class PaymentListView(generics.ListAPIView):
    serializer_class = MpesaCheckoutSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        timestamp = self.request.query_params.get('timestamp')
        if timestamp:
            queryset = Transaction.objects.filter(timestamp = timestamp)
        return queryset




class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = MpesaCheckoutSerializer






