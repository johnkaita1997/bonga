from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from school.models import School
from student.api.serializer import StudentSerializer
from student.models import Student

class StudentCreateView(generics.CreateAPIView):

    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    def perform_create(self, serializer):

        schoolid = self.request.query_params.get('schoolid')
        print(schoolid)
        school = School.objects.get(id = schoolid)
        if school:
            serializer.validated_data['school'] = school
        else:
            print("No school")
        if serializer.is_valid():
            serializer.save()
            return  Response({'details': "Student saved successfully"})
        else:
            raise ValueError("An error occured")



class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        contactuserid = self.request.query_params.get('contactuserid')
        if contactuserid:
            queryset = queryset.filter(contacts__contactuser__id=contactuserid)
            queryset = queryset.distinct()
        return queryset


class StudentListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'details': 'Student updated successfully'}, status=status.HTTP_200_OK)



class GetStudentWithUserIdView(APIView):
    serializer_class = StudentSerializer

    def get(self):
        userid = self.request.query_params.get('user')
        student = Student.objects.get(user = userid)
        if student:
            return Response(student)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Movie not found"})

