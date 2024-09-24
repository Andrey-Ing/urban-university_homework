from django.contrib import admin
from .models import Car, Airplane, Yacht, Demo
# Register your models here.

admin.site.register((Car, Airplane, Yacht, Demo), )
