from rest_framework import generics
from rest_framework.response import Response

from school.api.serializer import SchoolSerializer
from school.models import School

class SchoolCreateView(generics.CreateAPIView):

        serializer_class = SchoolSerializer

        def get_queryset(self):
            return School.objects.all()

        def perform_create(self, serializer):
            if serializer.is_valid():
                serializer.save()
                return Response({'details': "School saved successfully"})
            else:
                raise ValueError("An error occured")


class SchoolListView(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        return queryset


class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer