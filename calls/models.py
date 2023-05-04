from django.db import models

from student.models import Student


class DatingModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Call(DatingModel, models.Model):
    callstamp = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    tokensused = models.FloatField(max_length=255)
    minutesused = models.FloatField(max_length=255)
    mobileused = models.CharField(max_length=255, default="0700000000", blank=True, null=True)
    mobilecalled = models.CharField(max_length=255)
    personcalled = models.CharField(max_length=255, default="Admin", blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="calls", default=None)

    def __str__(self):
        return str(self.id) + f" -   Call Duration :  {self.duration}"


