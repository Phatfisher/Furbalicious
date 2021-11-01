from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    firstName = models.CharField(db_column='firstName', blank=False, null=False, max_length=80)
    lastName = models.CharField(db_column='lastName', blank=False, null=False, max_length=80)
    email = models.CharField(db_column='email', blank=False, null=False, max_length=200)
    isConfirmed = models.IntegerField(db_column='isConfirmed', null=False)
    password = models.CharField(db_column='password', null=False, max_length=200)
    lastLoginDate = models.DateTimeField(db_column='lastLoginDate')


class Furby(models.Model):
    furbyName = models.CharField(db_column='furbyName', blank=False, null=False, max_length=200)
    cost = models.FloatField(db_column="cost", null=False)
    description = models.CharField(db_column='description', max_length=5000)
    imagePath = models.CharField(db_column='imagePath', max_length=1000)