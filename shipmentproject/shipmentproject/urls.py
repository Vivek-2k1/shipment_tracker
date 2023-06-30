"""shipmentproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shipmentapp.views import home,cargo,tracking,shipment_list,delete_shipment,delete_cargo,delete_tracking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('cargo/<int:id>/',cargo,name="cargo"),
    path('tracking/<int:id>/',tracking,name="tracking"),
    path('shipment_list/',shipment_list,name="shipment_list"),
    path('delete_shipment/<int:id>/',delete_shipment,name="delete_shipment"),
    path('delete_cargo/<int:cargo_id>/',delete_cargo,name="delete_cargo"),
    path('delete_tracking/<int:tracking_id>/',delete_tracking,name="delete_tracking")
]
