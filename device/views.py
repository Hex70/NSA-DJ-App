from django.shortcuts import render,redirect
from django.db import models
from .models import Device
# Create your views here.
def index(request): 
    dev = Device.objects.all()
    context = {
       'dev' : dev
    }
    return render(request, 'device/Managedevices.html', context)
def add(request): 
    return render(request, 'device/add.html')


def deleteDevice(request,device_id): 
    devdel = Device.objects.get(id=device_id)
    
 #  if request.method == "POST":
    if request.method == "POST" :
        
        devdel.delete()
        return redirect('/device/')

    context = {'item':devdel}

    return render(request, 'device/delete.html', context)


#def deleteDevice(request, device_id):

#dev
	#devdel = Devices.objects.get(id=device_id)

#	if request.method == "POST":
#		devdel.delete()
#		return redirect('/devices/')

#	context = {'item':devdel}
#	device_ids=1
#    return render(request, 'devices/delete.html')
 