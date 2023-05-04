from rest_framework import serializers

from appuser.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):

    contact = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = AppUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
            'confirmpassword': {'write_only': True},
        }




