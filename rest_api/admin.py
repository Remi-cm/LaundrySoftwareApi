from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Shipper)
admin.site.register(models.Laundry)
admin.site.register(models.Clothe)
admin.site.register(models.Order)
admin.site.register(models.OrderLine)
