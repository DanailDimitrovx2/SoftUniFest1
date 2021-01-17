import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.db.models import Manager


class Department(models.Model):

    objects=Manager()

    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Position(models.Model):

    objects=Manager()

    name=models.CharField(max_length=50)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class News(models.Model):

    objects=Manager()

    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)
    date=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class UserManager(UserManager):

    def create_user(self, email, phone_number=None, first_name=None, last_name=None, password=None):
        """
        Creates and saves a User with the given properties.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number=None, first_name=None, last_name=None, password=None):
        """
        Creates and saves a superuser with the given properties.
        """
        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )
        update_fields = ['is_admin', 'is_superuser', 'is_active', 'is_staff']
        for attr in update_fields:
            setattr(user, attr, True)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserManager()

    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    position=models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)





    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    @property
    def full_name(self):
        """ Return user full name"""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):

        return self.email