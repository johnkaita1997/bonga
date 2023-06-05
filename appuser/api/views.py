from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from appuser.api.serializers import AppUserSerializer
from appuser.models import AppUser
from school.models import School


class AppUserCreateView(generics.CreateAPIView):
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        school_id = request.data.pop('school', None)  # Remove 'school' from request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if school_id:
            school = get_object_or_404(School, id=school_id)  # Retrieve the School instance
            serializer.validated_data['school'] = school
        self.perform_create(serializer)
        return Response({'details': 'User saved successfully'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        phone = serializer.validated_data['phone']
        fullname = serializer.validated_data['fullname']
        isstudent = serializer.validated_data['isstudent']
        isadmin = serializer.validated_data['isadmin']
        isparent = serializer.validated_data['isparent']
        isagent = serializer.validated_data['isagent']
        password = serializer.validated_data['password']
        confirmpassword = serializer.validated_data['confirmpassword']
        school = None
        try:
            school = serializer.validated_data['school']
        except:
            pass

        # validate email
        qs = AppUser.objects.filter(username=email)
        if qs.exists():
            raise serializers.ValidationError({'details': 'User already exists'})
        if password != confirmpassword:
            raise serializers.ValidationError({'details': 'Password and Confirm Password should be the same'})

        data = {
            "email": email,
            "username": email,
            "fullname": fullname,
            "phone": phone,
            "isstudent": isstudent,
            "isparent": isparent,
            "isadmin": isadmin,
            "isagent": isagent,
            "password": password,
            "confirmpassword": confirmpassword,
            "school": school
        }

        if 'school' in serializer.validated_data:
            schoolid = serializer.validated_data['school']
            data['school'] = schoolid

        user = AppUser.objects.create(**data)
        with transaction.atomic():
            user.set_password(password)
            user.save()
            data['details'] = "Registration was successful"
            # token = Token.objects.get(user=account).key
            # data['Authentication Token'] = token

        if serializer.is_valid():
            return Response(data)
        else:
            data = serializer.errors
            return Response(data)




class AppUserListView(generics.ListAPIView):
    serializer_class = AppUserSerializer

    def get_queryset(self):
        queryset = AppUser.objects.all()
        mobile = self.request.query_params.get('mobile')
        if mobile:
            queryset = AppUser.objects.filter(phone = mobile)
        return queryset



class AppUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'details': 'App User updated successfully'}, status=status.HTTP_200_OK)




class FineAppUserListView(generics.ListAPIView):
    serializer_class = AppUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = AppUser.objects.filter(id=user_id)
        return queryset