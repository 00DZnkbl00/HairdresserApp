from django.db import models


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)


class Client(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=254)


class Order(models.Model):
    code = models.CharField(max_length=32)
    paymentState = models.BooleanField()


class Session(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)


class Service(models.Model):
    name = models.CharField(max_length=16)
    price = models.FloatField()
