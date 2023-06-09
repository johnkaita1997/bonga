
from django.urls import path

from tokens.api.views import *

urlpatterns = [
    path('create', TokenCreateView.as_view(), name="token-create"),
    path('list/<int:pk>', TokenListView.as_view(), name="token-list"),
]
