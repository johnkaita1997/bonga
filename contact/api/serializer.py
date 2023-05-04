from rest_framework import serializers

from appuser.api.serializers import AppUserSerializer
from calls.api.serializer import CallsSerializer
from contact.models import Contact, DatingModel
from school.api.serializer import SchoolSerializer
from student.models import Student


class StudentSerializerImported(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    calls = CallsSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    # contactuser = AppUserSerializer(read_only=True)
    students = StudentSerializerImported(read_only=True, many=True)
    class Meta:
        model = Contact
        fields = "__all__"



class StudentSerializerImportedWeb(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('contacts','fullname',)

class ContactsWeberializer(serializers.ModelSerializer):
    # contactuser = AppUserSerializer(read_only=True)
    students = StudentSerializerImportedWeb(read_only=True, many=True)

    class Meta:
        model = Contact
        fields = ('name',
                  'mobile',
                  'id',
                  'relationship',
                  'students',
                  'mobile',)
