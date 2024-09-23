from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=20)


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    max_speed = models.IntegerField()


class Yacht(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
