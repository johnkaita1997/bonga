from rest_framework import serializers

from appuser.api.serializers import AppUserSerializer
from appuser.models import AppUser
from mobile.api.serializers import MobileSerializer
from school.models import School
from student.models import Student


class SchoolSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), many=True)
    agents = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=True)
    mobile = MobileSerializer()

    class Meta:
        model = School
        fields = "__all__"




class SchoolWebSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True)
    agents = AppUserSerializer(many=True)
    num_students = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()
    mobile = MobileSerializer()

    class Meta:
        model = School
        fields = "__all__"

    def get_num_students(self, obj):
        return obj.students.count()

    def get_code(self, obj):
        return f"{obj.id}{obj.name[:3].upper()}"






