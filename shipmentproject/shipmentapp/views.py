from django.shortcuts import render,redirect
from .models import ShipmentModel,CargoModel,TrackingModel
from .forms import ShipmentForm,CargoForm,TrackingForm
from datetime import datetime

# Create your views here.
def home(request):
    shipments = ShipmentModel.objects.all()
    if request.method == "POST":
        data = ShipmentForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Shipment Created"
            fm = ShipmentForm()
            context = {
                "shipments":shipments,
                "fm":fm,
                "msg":msg
            }
            return render(request,'home.html',context)
        else:
            msg = data
            context = {
                "shipments":shipments,
                "msg":msg
            }
            return render(request,'home.html',context)
    else:
        fm = ShipmentForm
        context = {
                "shipments":shipments,
                "fm":fm
            }
        return render(request,'home.html',context)
    
def cargo(request,id):
    shipment = ShipmentModel.objects.get(id=id)
    cargos = CargoModel.objects.filter(shipment=shipment)
    if request.method == "POST":
        data = CargoForm(request.POST)
        if data.is_valid():
            new_data = data.save(commit=False)
            new_data.shipment = shipment
            new_data.save()
            msg = "Cargo Created"
            fm = CargoForm()
            context = {
                "fm":fm,
                "msg":msg,
                "cargos":cargos
            }
            return render(request,'cargo.html',context)
        else:
            msg = data
            context = {
                "msg":msg,
                "cargos":cargos
            }
            return render(request,'cargo.html',context)
    else:
        fm = CargoForm()
        return render(request,'cargo.html',{"fm":fm,"cargos":cargos})
    
def tracking(request,id):
    shipment = ShipmentModel.objects.get(id=id)
    trackings = TrackingModel.objects.filter(shipment=shipment)
    if request.method == "POST":
        data = TrackingForm(request.POST)
        if data.is_valid():
            new_data = data.save(commit=False)
            new_data.shipment = shipment
            if new_data.status == 'DELIVERED':
                shipment.actual_delivery_date = datetime.now().date()
            shipment.save()
            new_data.save()
            msg = "Track Created"
            return redirect('home')
        else:
            msg = data
            context = {
                "msg":msg,
                "trackings":trackings
            }
            return render(request,'tracking.html',context)
    else:
        fm = TrackingForm()
        return render(request,'tracking.html',{"fm":fm,"trackings":trackings})

def shipment_list(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    status = request.GET.get('status')

    shipments = ShipmentModel.objects.order_by('expected_delivery_date')
    if origin:
        shipments = shipments.filter(origin=origin)

    if destination:
        shipments = shipments.filter(destination=destination)

    if status:
        shipments = shipments.filter(status=status)

    return render(request, 'shipment_list.html', {'shipments': shipments})

def delete_shipment(request,id):
    shipment = ShipmentModel.objects.get(id=id)
    shipment.delete()
    return redirect('home')

def delete_cargo(request,cargo_id):
    cargo = CargoModel.objects.get(id=cargo_id)
    cargo.delete()
    return redirect('home')

def delete_tracking(request,tracking_id):
    track = TrackingModel.objects.get(id=tracking_id)
    track.delete()
    return redirect('home')