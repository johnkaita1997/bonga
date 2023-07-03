from django.db import models

from school.models import School

id = models.AutoField(primary_key=True)


class Constant(models.Model):
    id = models.AutoField(primary_key=True)
    activationamount = models.IntegerField(default=0, blank=True, null=True)
    tokennumber = models.IntegerField(default=1, blank=True, null=True)
    minutespertokenOrequivalentminutes = models.FloatField(max_length=255, default=0)
    minutepershilling = models.FloatField(max_length=255, default=0)
    shillingspertokenOrequivalentshillings = models.FloatField(max_length=255, default=0,  blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="constants", default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id) + f" -   Activation Constant :  {self.activationamount}"