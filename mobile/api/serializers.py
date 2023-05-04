from rest_framework import serializers

from mobile.models import Mobile
from school.models import School


class MobileSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Mobile
        fields = "__all__"

