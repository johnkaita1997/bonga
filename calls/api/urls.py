from django.urls import path

from calls.api.views import *

urlpatterns = [
    path('create', CallsCreateView.as_view(), name="call-create"),
    path('list', CallsListView.as_view(), name="call-list"),
    path('<int:pk>', CallsDetailView.as_view(), name="call-detail"),
]
