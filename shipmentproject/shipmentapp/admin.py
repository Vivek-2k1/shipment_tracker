from django.contrib import admin
from .models import ShipmentModel,CargoModel,TrackingModel

# Register your models here.
admin.site.register(ShipmentModel)
admin.site.register(CargoModel)
admin.site.register(TrackingModel)