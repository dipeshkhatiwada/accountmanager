from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, contact_no, first_name=None, last_name=None,  password=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(
            email=self.normalize_email(email),
            contact_no=contact_no,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name=None,last_name=None, contact_no='987654321', password=None):
        user = self.create_user(email, first_name, last_name, contact_no, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Enter your email",
        unique=True
    )
    contact_no = models.CharField(
        max_length=20,
        verbose_name="Contact Number",
        # default='987654321',
        unique=True
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="First Name",
        null=True, blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="last Name",
        null=True, blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_level):
        return True

    @property
    def is_staff(self):
        return self.is_admin
