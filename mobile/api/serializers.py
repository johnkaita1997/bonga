from rest_framework import serializers

from mobile.models import Mobile
from school.models import School


class MobileSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Mobile
        fields = ['id', 'standingtoken', 'standingminutes', 'tokensconsumed', 'active', 'mobile', 'minutesconsumed', 'school']

    def get_school(self, obj):
        return obj.school.name

