from django.db import models

from school.models import School


class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



# Create your models here.
class Mobile(DatingModel, models.Model):
    standingtoken = models.FloatField(max_length=255, default=0.0, blank=True, null=True)
    standingminutes = models.FloatField(max_length=255, default=0.0, blank=True, null=True)
    tokensconsumed = models.FloatField(max_length=255, default=0.0, blank=True, null=True)
    minutesconsumed = models.FloatField(max_length=255, default=0.0, blank=True, null=True)
    school =  models.ForeignKey(School, on_delete=models.CASCADE, null=True, related_name="mobiles")
    active = models.BooleanField(max_length=255, default=True)
    mobile = models.CharField(max_length=255)

    class Meta:
        ordering = ["-date_created"]
        app_label = "mobile"

    def __str__(self):
        return str(self.mobile)




# Create your models here.
class SchoolWebCreate(DatingModel, models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="schoolwebcreate", default=None)


    class Meta:
        ordering = ["-date_created"]
        app_label = "school"

    def __str__(self):
        return f"{self.name}"
