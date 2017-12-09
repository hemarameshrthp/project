from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from rest_framework.renderers import JSONRenderer
from .serilizer import MachineStatusSer,IdleSer,RunSer,SettingSer
from .models import MachineStatus,Idle,Run,Setting
from csv import writer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def main(request):
    return render(request,"UI/main.html")
def idleline(request):
    return render(request,"UI/idleline.html")
def runline(request):
    return render(request,"UI/runline.html")
def settingline(request):
    return render(request,"UI/settingline.html")
def  home(request):
    return render(request,"UI/home.html")

def notloggined(request):
    if request.method =="GET":
        return render(request, "UI/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/home/")

def register(request):
    if request.method == "GET":
        return render(request,"UI/register.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user.is_active:
            login(request,user)
            return render(request, "UI/home.html")

def machinestatus(request):
    objs = MachineStatus.objects.all()
    serobj = MachineStatusSer(objs, many=True)
    return JsonResponse(serobj.data, safe=False)
def idle(request):
    objs = Idle.objects.all()
    serobj = IdleSer(objs, many=True)
    return JsonResponse(serobj.data, safe=False)
def run(request):
    objs = Run.objects.all()
    serobj = RunSer(objs, many=True)
    return JsonResponse(serobj.data, safe=False)
def setting(request):
    objs = Setting.objects.all()
    serobj = SettingSer(objs, many=True)
    return JsonResponse(serobj.data, safe=False)

@csrf_exempt
def postdata(request):
    if request.method == "POST":
        status = request.POST['status']
        ms = MachineStatus(status=status)
        ms.save()
        JsonResponse(u'updated')
    JsonResponse(u'error lol')