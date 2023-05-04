from rest_framework import serializers

from appuser.models import AppUser
from payments.models import *


class MpesaCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['student']


    def validate(self, data):
        studentid = data.get('studentid')
        mobile = data.get('mobile')
        amount = data.get('amount')
        timestamp = data.get('timestamp')

        if not studentid:
            raise serializers.ValidationError('Student Id is required')
        if not amount:
            raise serializers.ValidationError('Amount is required')
        if not mobile:
            raise serializers.ValidationError('Mobile is required')
        if not timestamp:
            raise serializers.ValidationError('Timestamp is required')

        return data