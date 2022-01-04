from django.shortcuts import render
import requests 
from main.models import plcp
from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def index(request):
	data=plcp.objects.all().order_by('-pk')
	dtt=[]
	V=[]
	I=[]
	P=[]
	for i in data:
		dtt.append(str(i.dt))
		V.append(i.Voltage)
		I.append(i.Current)
		P.append(i.Power)
	return render(request,'index.html',{'data':data,'V':V,'I':I,'dtt':dtt,'P':P})

@csrf_exempt
def transmit(request):
    if request.method=="POST":
        print(request.POST)
        dt=request.POST.get("dt")
        V=request.POST.get("V")
        I=request.POST.get("I")
        P=request.POST.get("P")
        plcp(dt=dt,Voltage=V,Current=I,Power=P).save()
        return HttpResponse("SUCCESS")