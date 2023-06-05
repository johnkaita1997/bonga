from rest_framework import serializers

from appuser.models import AppUser
from mobile.api.serializers import MobileSerializer
from school.models import School


class mySchoolSerializer(serializers.ModelSerializer):
    # A comment
    students = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), many=True)
    agents = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=True)

    class Meta:
        model = School
        fields = "__all__"


class AppUserSerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    school = mySchoolSerializer(read_only=True)

    class Meta:
        model = AppUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
            'confirmpassword': {'write_only': True},
        }




