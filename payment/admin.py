from django.contrib import admin

# Register your models here.

from payment import models

admin.site.register(models.Order)
