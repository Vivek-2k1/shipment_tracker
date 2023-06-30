from django import forms
from .models import ShipmentModel,CargoModel,TrackingModel

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = ShipmentModel
        fields = ['origin','destination','expected_delivery_date','actual_delivery_date']
        widgets = {
            'expected_delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = CargoModel
        fields = ['name','quantity']
        
class TrackingForm(forms.ModelForm):
    class Meta:
        model = TrackingModel
        fields = ['status','location']