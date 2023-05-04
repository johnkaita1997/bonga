from django.urls import path

from constants.api.views import *

urlpatterns = [
    path('create', ConstantCreateView.as_view(), name="constant-create"),
    path('list', ConstantListView.as_view(), name="constant-list"),
    path('<int:pk>', ConstantDetailView.as_view(), name="constant-detail"),
]
