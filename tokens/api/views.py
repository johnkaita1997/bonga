from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from constants.models import Constant
from tokens.api.serializers import TokenSerializer
from tokens.models import Token


class TokenCreateView(generics.CreateAPIView):
    serializer_class = TokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokenamount = serializer.validated_data['tokenamount']

        present = Token.objects.filter(tokenamount=tokenamount)
        if present:
            return Response({'details': "Token already exists"})

        shillingspertokenOrequivalentshillings = Constant.objects.first().shillingspertokenOrequivalentshillings
        equivalentshillings = shillingspertokenOrequivalentshillings * tokenamount
        serializer.validated_data['equivalentshillings'] = equivalentshillings
        self.perform_create(serializer)
        return Response({'details': 'Token saved successfully'}, status=status.HTTP_201_CREATED)


    def perform_create(self, serializer):
        serializer.save()



class TokenListView(generics.ListAPIView):
    serializer_class = TokenSerializer

    def get_queryset(self):
        queryset = Token.objects.all()
        return queryset
