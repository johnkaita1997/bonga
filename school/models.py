import uuid

from django.db import models

from mobile.models import Mobile


class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class School(DatingModel, models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='school', null=True, blank=True)

    class Meta:
        ordering = ["-date_created"]
        app_label = "school"

    def __str__(self):
        return f"{self.id} - {self.name}"


# Create your models here.
class SchoolWebCreate(DatingModel, models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="schoolwebcreate", default=None)


    class Meta:
        ordering = ["-date_created"]
        app_label = "school"

    def __str__(self):
        return f"{self.name}"
