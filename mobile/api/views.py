from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from constants.models import Constant
from mobile.api.serializers import MobileSerializer
from mobile.models import Mobile


class MobileCreateView(generics.CreateAPIView):
    serializer_class = MobileSerializer

    def get_queryset(self):
        return Mobile.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response({'details': "Mobile saved successfully"})
        else:
            raise ValueError("An error occured")


class MobileListView(generics.ListAPIView):
    serializer_class = MobileSerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        return queryset



class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        school = instance.school  # Get the associated school
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'standingminutes' in serializer.validated_data:
            try:
                tokenperminutes = Constant.objects.get(school = school).minutespertokenOrequivalentminutes
                serializer.validated_data['standingtoken'] = tokenperminutes * serializer.validated_data['standingminutes']

                oldstandingminutes = instance.standingminutes
                oldstandingtoken = instance.standingtoken

                newtoken = serializer.validated_data['standingtoken']
                newminutes = serializer.validated_data['standingminutes']

                instance.standingtoken = oldstandingtoken + newtoken
                instance.standingminutes = oldstandingminutes + newminutes
                instance.save()

                return Response({'details': "Mobile saved successfully"})

            except ObjectDoesNotExist:
                return Response({'details': "Constant Objects have not been saved"})

        else:
            return Response({'details': "Minutes Cannot Be Zero"})


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'standingminutes' in serializer.validated_data and 'standingtoken' in serializer.validated_data:
            try:
                oldstandingminutes = instance.standingminutes
                oldstandingtoken = instance.standingtoken

                userminutes = serializer.validated_data['standingminutes']
                usertoken = serializer.validated_data['standingtoken']

                instance.standingtoken = oldstandingtoken - usertoken
                instance.standingminutes = oldstandingminutes - userminutes
                instance.save()

                return Response({'details': "Mobile Updated successfully"})

            except ObjectDoesNotExist:
                return Response({'details': "Constant Objects have not been saved"})
        else:
            return Response({'details': "Both New Minutes and Tokens required"})



class MobileIdDetailView(APIView):
    def get(self, request, pk):
        mobile = Mobile.objects.get(mobile=pk)
        return Response(str(mobile.id))