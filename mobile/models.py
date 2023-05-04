from django.db import models

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
    active = models.BooleanField(max_length=255, default=True)
    mobile = models.CharField(max_length=255)

    class Meta:
        app_label = "mobile"

    def __str__(self):
        return str(self.id) + f" - {self.mobile}"