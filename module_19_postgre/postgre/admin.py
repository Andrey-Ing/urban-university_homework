from django.contrib import admin

# Register your models here.
from .models import Car, Airplane, Yacht, Money, Users
# Register your models here.

admin.site.register((Car, Airplane, Yacht, Money, Users), )
