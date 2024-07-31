from django.db import models


# Create your models here.

class Buyer(models.Model):  # модель представляет покупателя
    name = models.CharField(max_length=20)  # имя покупателя
    balance = models.DecimalField(max_digits=16, decimal_places=2)  # баланс
    age = models.PositiveSmallIntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена игры
    size = models.DecimalField(max_digits=15, decimal_places=3)  # размер файлов игры
    description = models.TextField()  # описание
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer)  # покупатели игры
