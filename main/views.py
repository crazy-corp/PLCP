from django.shortcuts import render
import requests 
from main.models import plcp,plcp_state
from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect , reverse
import csv
# Create your views here.

def index_state(request):
	state1=plcp_state.objects.get(id=1)
	if(state1.state==True):
		state1.state=False
		state1.save()
	else:
		state1.state=True
		state1.save()

	return redirect("home")
def index(request):
	data=plcp.objects.all().order_by('-pk')
	state1=plcp_state.objects.all().first().state
	dtt=[]
	V=[]
	I=[]
	P=[]
	for i in data:
		dtt.append(str(i.dt))
		V.append(i.Voltage)
		I.append(i.Current)
		P.append(i.Power)
	return render(request,'index.html',{'data':data,'V':V,'I':I,'dtt':dtt,'P':P,'state':state1})

def load2(request):
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
	return render(request,'load2.html',{'data':data,'V':V,'I':I,'dtt':dtt,'P':P})

def load3(request):
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
	return render(request,'load3.html',{'data':data,'V':V,'I':I,'dtt':dtt,'P':P})

def load4(request):
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
	return render(request,'load4.html',{'data':data,'V':V,'I':I,'dtt':dtt,'P':P})

def red(request):
	return redirect('/')

def cs(request):
	response = HttpResponse(content_type='test/csv')
	response['Content-Disposition']='attachment; filename = data1.csv'
	data=plcp.objects.all().order_by('-pk')
	writer =csv.writer(response)
	writer.writerow(['DateTime','Voltage','Current','PF','Power'])
	for i in data:
		writer.writerow([str(i.dt),i.Voltage,i.Current,i.pf,i.Power])
	return response


@csrf_exempt
def transmit(request):
    if request.method=="POST":
        print(request.POST)
        dt=request.POST.get("dt")
        V=request.POST.get("V")
        I=request.POST.get("I")
        P=request.POST.get("P")
        plcp(dt=dt,Voltage=V,Current=I,Power=P).save()
        state1=plcp_state.objects.all().first().state
        return JsonResponse({"TransMit":"SUCCESS","state":state1})