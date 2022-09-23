from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *
from django.utils import timezone
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=11)
    is_admin = models.BooleanField(default=False)
    Avatar = models.ImageField(upload_to="images/Avatar",blank=True,null=True)


    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    def name(self):
        return str(self.username)