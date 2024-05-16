from django.db import models
from .validators import validate_time_interval


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Client(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Order(models.Model):
    code = models.CharField(max_length=32)
    paymentState = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class Session(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(validators=[validate_time_interval], null=True)

    def __str__(self):
        return f"{self.date} {self.time}"


class Service(models.Model):
    name = models.CharField(max_length=16)
    price = models.FloatField()

    def __str__(self):
        return self.name
