from django.db import models
from appuser.models import BaseModel, AppUser
from student.models import Student

STATUS = [
    ("PENDING", "PENDING"),
    ("COMPLETE", "COMPLETE"),
    ("CANCELLED", "CANCELLED"),
    ("FAILED", "FAILED"),
]

PURPOSE = [
    ("REGISTRATION", "REGISTRATION"),
    ("TOKEN", "TOKEN")
]


class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Transaction(DatingModel, models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, related_name='usertransactions')
    date_created = models.DateTimeField(auto_now_add=True)
    studentid = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField(default=0.0)
    mobile = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=STATUS, default="PENDING")
    reference = models.CharField(max_length=100, blank=True, null=True)
    receiptnumber = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    checkoutid = models.CharField(max_length=255,  blank=True, null=True)
    timestamp = models.CharField(max_length=255, default="0000000000",  blank=True, null=True)
    purpose = models.CharField(max_length=255,  choices=PURPOSE, default="REGISTRATION")
    student =  models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name="studenttransactions")

    class Meta:
        ordering = ["-date_created"]
        app_label = "payments"

    def __str__(self):
        return  f"{self.id}      -      " + self.mobile + f"    -      {self.date_created}"

