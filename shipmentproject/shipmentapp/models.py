from django.db import models

# Create your models here.
class ShipmentModel(models.Model):
    origin = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
    expected_delivery_date = models.DateField()
    actual_delivery_date = models.DateField(null=True,blank=True)
    STATUS_CHOICES = [
        ('ER','EnRoute'),
        ('EA','Early'),
        ('DE','Delayed'),
        ('OT','OnTime'),
    ]
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default='ER')

    def save(self,*args,**kwargs):
        if self.actual_delivery_date:
            if self.actual_delivery_date < self.expected_delivery_date:
                self.status = 'EA'
            elif self.actual_delivery_date > self.expected_delivery_date:
                self.status = 'DE'
            else:
                self.status = 'OT'
        else:
            self.status = 'ER'
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
class CargoModel(models.Model):
    shipment = models.ForeignKey(ShipmentModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.shipment} {self.name}"
    
class TrackingModel(models.Model):
    shipment = models.OneToOneField(ShipmentModel,on_delete=models.CASCADE)
    Status_Choices = [
        ('PACK', 'Packing'),
        ('ARRIVED', 'Arrived At'),
        ('DISPATCHED', 'Dispatched From'),
        ('DELIVERED', 'Delivered'),
    ]
    status = models.CharField(max_length=20,choices=Status_Choices)
    location = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.status} {self.location}"