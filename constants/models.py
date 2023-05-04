from django.db import models


# Create your models here.
class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Constant(DatingModel, models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    activationamount = models.IntegerField(default=0, blank=True, null=True)
    tokennumber = models.IntegerField(default=1, blank=True, null=True)

    minutespertokenOrequivalentminutes = models.FloatField(max_length=255, default=0)
    minutepershilling = models.FloatField(max_length=255, default=0)

    shillingspertokenOrequivalentshillings = models.FloatField(max_length=255, default=0,  blank=True, null=True)

    def __str__(self):
        return str(self.id) + f" -   Activation Constant :  {self.activationamount}"