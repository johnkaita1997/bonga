from rest_framework import generics
from rest_framework.response import Response

from appuser.models import AppUser
from contact.api.serializer import ContactSerializer
from contact.models import Contact


class ContactCreateView(generics.CreateAPIView):

    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all()

    def perform_create(self, serializer):

        user = serializer.validated_data['useractive']
        print(f'user id is {user}')

        if serializer.is_valid():
            serializer.save()
            return  Response({'details': "Contact saved successfully"})
        else:
            raise ValueError("An error occured")



class ContactListView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):

        contactuserid = self.request.query_params.get('contactuser')
        if contactuserid:
            print("Here arrived")
            user = AppUser.objects.get(id=contactuserid)
            queryset = Contact.objects.filter(contactuser=user)
            print(f"Queryset is {len(queryset)}")

            return queryset

        print("There arrived")
        queryset = Contact.objects.all()
        print(len(queryset))
        return queryset



class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer