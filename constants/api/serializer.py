from rest_framework import serializers

from constants.models import Constant
from web.forms import GlobalSettingsModel


class ConstantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constant
        fields = "__all__"


class GlobalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSettingsModel
        fields = "__all__"
