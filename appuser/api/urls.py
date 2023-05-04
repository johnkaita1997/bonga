from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from appuser.api.views import *
urlpatterns = [

    path('register/', AppUserCreateView.as_view(), name='register'),

    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('list', AppUserListView.as_view(), name="appuser-list"),
    path('userdetails', FineAppUserListView.as_view(), name="userdetails-list"),

    path('<str:pk>', AppUserDetailView.as_view(), name="appuser-detail"),

]





