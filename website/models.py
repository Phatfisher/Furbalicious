from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    firstName = models.CharField(db_column='firstName', blank=False, null=False, max_length=80)
    lastName = models.CharField(db_column='lastName', blank=False, null=False, max_length=80)
    email = models.CharField(db_column='email', blank=False, null=False, max_length=200)
    isConfirmed = models.IntegerField(db_column='isConfirmed', null=True)
    password = models.CharField(db_column='password', null=False, max_length=200)
    lastLoginDate = models.DateTimeField(db_column='lastLoginDate',  null=True)

class Furby(models.Model):
    furbyName = models.CharField(db_column='furbyName', blank=False, null=False, max_length=200)
    cost = models.FloatField(db_column="cost", null=False)
    description = models.CharField(db_column='description', max_length=5000)
    imagePath = models.CharField(db_column='imagePath', max_length=1000)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(null=False, db_column='orderDate')
    cardNumber = models.IntegerField(null=False, db_column='cardNumber')
    cardExpiry = models.CharField(null = False, db_column='cardExpiry', max_length=10)
    shippingStreetAddress = models.CharField(null = False, db_column='shippingStreetAddress', max_length=500)
    shippingCity = models.CharField(null = False, db_column='shippingCity', max_length=100)
    shippingState = models.CharField(null = False, db_column='shippingState', max_length=100)
    shippingZip = models.CharField(null = False, db_column='shippingZip', max_length=20)
    shippingCountry = models.CharField(null = False, db_column='shippingCountry', max_length=200)

class OrderFurbies(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    furby = models.ForeignKey(Furby, on_delete=models.CASCADE)

