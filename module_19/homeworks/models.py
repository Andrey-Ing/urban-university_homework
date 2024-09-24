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


class Demo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hint = models.TextField(db_column='Hint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demo'


