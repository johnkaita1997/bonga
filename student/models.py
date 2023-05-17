import uuid

from django.db import models

from appuser.models import AppUser
from contact.models import Contact
from school.models import School



class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Student(DatingModel, models.Model):
    fullname = models.CharField(max_length=255)

    kcpeindexnumber = models.CharField(max_length=255, blank=True, null=True)
    registrationnumber = models.CharField(max_length=255, blank=True, null=True)

    active = models.BooleanField(max_length=255, default=False)

    activefromdate = models.DateTimeField(blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)

    password = models.CharField(max_length=255, null=True, blank=True, default="one")
    confirmpassword = models.CharField(max_length=255, null=True, blank=True, default="one")

    tokenbalance = models.FloatField(default=0.00, blank=True, null=True)
    totalnumberofcalls = models.FloatField(default=0.00, blank=True, null=True)

    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students", default=None, null=True, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='students', default=None)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='student')


    class Meta:
        ordering = ["-date_created"]
        app_label = "student"

    def __str__(self):
        return  f"{str(self.id)} - {self.fullname}"





