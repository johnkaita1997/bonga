from django.urls import path

from mobile.api.views import *

urlpatterns = [
    path('create', MobileCreateView.as_view(), name="mobile-create"),
    path('list', MobileListView.as_view(), name="mobile-list"),
    path('<int:pk>', MobileDetailView.as_view(), name="mobile-detail"),
    path('id/<int:pk>', MobileIdDetailView.as_view(), name="myschoolmy-detail"),
    path('balance/<int:pk>', MobileTokenMinutesBalance.as_view(), name="MobileTokenMinutesBalance-detail"),
]
