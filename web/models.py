from django.db import models
from django.forms import forms


# Create your models here.
class ImportStudentModel(models.Model):
    student_fullname_table_name = models.CharField(max_length=255, blank=True, null=True,default=None)
    student_firstname_table_name =  models.CharField(max_length=255, blank=True, null=True,default=None)
    student_middlename_table_name =  models.CharField(max_length=255, blank=True, null=True,default=None)
    student_lastname_table_name =  models.CharField(max_length=255, blank=True, null=True,default=None)

    student_admission_number_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    student_kcpeindex_number_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)

    parent_fullname_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    parent_phone_number_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)

    contact_person_one_fullname_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    contact_person_one_mobile_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)

    contact_person_two_fullname_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    contact_person_two_mobile_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)

    contact_person_three_fullname_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    contact_person_three_mobile_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)

    header_row_number = models.IntegerField(max_length=255, default=None)

    def __str__(self):
        return f"{self.student_fullname_table_name}"



# Create your models here.
class ImportParentModel(models.Model):
    parent_fullname_table_name =  models.CharField(max_length=255, blank=True, null=True,default=None)
    parent_phone_number_table_name = models.CharField(max_length=255, blank=True, null=True,default=None)
    mobiletwo_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    email_table_name  =  models.CharField(max_length=255, blank=True, null=True,default=None)
    header_row_number = models.IntegerField(max_length=255, default=None)

    def __str__(self):
        return f"{self.parent_fullname_table_name}"