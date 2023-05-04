from rest_framework import serializers

from constants.models import Constant


class ConstantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constant
        fields = "__all__"
