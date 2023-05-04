from django.urls import path, include

from contact.api.views import ContactListView, ContactCreateView, ContactDetailView

urlpatterns = [
    path('create', ContactCreateView.as_view(), name="contact-create"),
    path('list', ContactListView.as_view(), name="contact-list"),
    path('<int:pk>', ContactDetailView.as_view(), name="contact-detail"),
]
