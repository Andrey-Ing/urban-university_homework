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


class Money(models.Model):
    value = models.IntegerField()
    currency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Money'


class Users(models.Model):
    user = models.TextField(db_column='User')  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
