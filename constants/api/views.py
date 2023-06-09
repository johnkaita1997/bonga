from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from constants.api.serializer import ConstantSerializer, GlobalSettingsSerializer
from constants.models import Constant
from web.forms import GlobalSettingsModel


class ConstantCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConstantSerializer

    def get_queryset(self):
        return Constant.objects.all()

    def perform_create(self, serializer):
        if 'minutespertokenOrequivalentminutes' not in serializer.validated_data or 'minutepershilling' not in serializer.validated_data:
            raise serializers.ValidationError({'details': 'Both MinutesPerToken and MinutesPerShilling required'})

        minutespertokenOrequivalentminutes = serializer.validated_data['minutespertokenOrequivalentminutes']
        minutepershilling = serializer.validated_data['minutepershilling']

        shillingspertokenOrequivalentshillings = minutespertokenOrequivalentminutes / minutepershilling
        serializer.validated_data['shillingspertokenOrequivalentshillings'] = shillingspertokenOrequivalentshillings
        serializer.validated_data['id'] = 0

        all_objects = Constant.objects.all()
        all_objects.delete()

        if serializer.is_valid():
            serializer.save()
            return  Response({'details': "Constant saved successfully"})
        else:
            raise ValueError("An error occured")



class ConstantListView(generics.ListAPIView):
    serializer_class = ConstantSerializer

    def get_queryset(self):
        school = self.request.query_params.get('school')
        queryset = Constant.objects.filter(school=school)
        return queryset



class ConstantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Constant.objects.all()
    serializer_class = ConstantSerializer



class GlobalSettingsListView(generics.ListAPIView):
    serializer_class = GlobalSettingsSerializer
    def get_queryset(self):
        queryset = GlobalSettingsModel.objects.filter(id=0)
        return queryset
