
from django.db import models

from school.models import School


# Create your models here.
class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Token(DatingModel, models.Model):
    tokenamount = models.IntegerField(default=0, blank=True, null=True)
    equivalentshillings = models.FloatField(default=0, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="tokens", default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id) + f" -   Token Amount :  {self.tokenamount}"

    class Meta:
        ordering = ["-date_created"]