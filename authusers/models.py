from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserType(models.TextChoices):
    STAFF =  'ST', 'Staff'
    ADMIN = 'AD', 'Admin'


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("User should have email")
        user = self.model(email= self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError("User must have Password")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.user_type = UserType.ADMIN
        user.save()
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=True, blank=True,unique=True)
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.STAFF)
    email = models.CharField(verbose_name="Email or Phone", max_length=255, unique=True, db_index=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}'

    def get_user_type(self):
        return f'{self.user_type}'

