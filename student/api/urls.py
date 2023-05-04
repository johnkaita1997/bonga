from django.urls import path

from student.api.views import *

urlpatterns = [
    path('create/', StudentCreateView.as_view(), name='create'),
    path('list', StudentListView.as_view(), name='student-list'),
    path('<int:pk>', StudentListDetailView.as_view(), name="student-detail"),
]

