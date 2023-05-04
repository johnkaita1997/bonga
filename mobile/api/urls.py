from django.urls import path

from mobile.api.views import *

urlpatterns = [
    path('create', MobileCreateView.as_view(), name="mobile-create"),
    path('list', MobileListView.as_view(), name="mobile-list"),
    path('<int:pk>', MobileDetailView.as_view(), name="mobile-detail")
]
