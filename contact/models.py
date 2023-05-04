from django.db import models

from appuser.models import AppUser


RELATIONSHIP = [
    ("PARENT", "PARENT"),
    ("GUARDIAN", "GUARDIAN"),
    ("SPONSOR", "SPONSOR"),
]


class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Contact(DatingModel, models.Model):
    relationship = models.CharField(max_length=255, choices=RELATIONSHIP, default="PARENT")
    mobile = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobiletwo = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    contactuser = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="contact")

    def __str__(self):
        return f"{self.id} - {self.name}"


