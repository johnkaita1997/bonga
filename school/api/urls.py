from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from school.api.views import *

urlpatterns = [
    path('create', SchoolCreateView.as_view(), name='school-create'),
    path('list', SchoolListView.as_view(), name="school-list"),
    path('<int:pk>', SchoolDetailView.as_view(), name="school-detail"),
    # path('standingtoken/<int:pk>', StandingTokenDetailView.as_view(), name="myschool-detail"),
    path('standingtoken/<int:pk>', StandingTokenDetailView.as_view(), name="myschool-detail"),
]
