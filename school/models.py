from django.db import models


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

    class Meta:
        ordering = ["-date_created"]
        app_label = "school"

    def __str__(self):
        return f"{self.id} - {self.name}"
