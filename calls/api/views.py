from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from calls.api.serializer import CallsSerializer
from calls.models import Call
from mobile.models import Mobile
from student.models import Student


class CallsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CallsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        minutesused = serializer.validated_data['minutesused']
        tokensused = serializer.validated_data['tokensused']
        mobileused = serializer.validated_data['mobileused']
        mobilecalled = serializer.validated_data['mobilecalled']
        self.perform_create(serializer)

        if Mobile.objects.filter(mobile=mobilecalled).first():
            print(f"Mobile Found For Mobile {mobilecalled}")
            mobileObj = Mobile.objects.get(mobile=mobilecalled)
            mobileObj.standingtoken = mobileObj.standingtoken - tokensused
            mobileObj.standingminutes = mobileObj.standingminutes - minutesused
            mobileObj.tokensconsumed = mobileObj.tokensconsumed + tokensused
            mobileObj.minutesconsumed = mobileObj.minutesconsumed + minutesused
            mobileObj.save()
        else:
            print(f"Mobile Not Found For Mobile {mobilecalled}")

        return Response({'details': 'Call log saved successfully'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class CallsListView(generics.ListAPIView):
    serializer_class = CallsSerializer

    def get_queryset(self):
        student = Student.objects.get(id=3)
        calls = student.call_set().all()

        print(calls)

        queryset = Call.objects.all()
        return queryset


class CallsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallsSerializer
