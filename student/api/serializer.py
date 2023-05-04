from rest_framework import serializers

from calls.api.serializer import CallsSerializer
from contact.api.serializer import ContactSerializer
from school.api.serializer import SchoolSerializer
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    contacts = ContactSerializer(many=True)
    calls = CallsSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = "__all__"


