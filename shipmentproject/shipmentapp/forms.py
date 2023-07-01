from django import forms
from .models import ShipmentModel,CargoModel,TrackingModel

class ShipmentForm(forms.ModelForm):
    origin = forms.CharField(label='Origin')
    destination = forms.CharField(label='Destination')
    expected_delivery_date = forms.DateField(label='Expected Delivery')
    actual_delivery_date = forms.DateField(label='Actual Delivery')
    status = forms.ChoiceField(label='Status')
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