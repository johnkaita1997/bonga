import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from appuser.managers import CustomUserManager
from school.models import School


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_joined= models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True



class AppUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    username = models.EmailField(unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    confirmpassword = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    fullname = models.CharField(max_length=255, blank=True, null=True)
    isstudent = models.BooleanField(default=False)
    isadmin = models.BooleanField(default=False)
    isparent = models.BooleanField(default=False)
    isagent = models.BooleanField(default=False)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="agents", default=None, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ["-date_created"]



