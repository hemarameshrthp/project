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
# Create your views here.

def main(request):
    return render(request,"UI/main.html")
def idleline(request):
    if request.method =="GET":
        return render(request,"UI/idleline.html")
    else:
        return HttpResponseRedirect('/home')

def runline(request):
    if request.method =="GET":
        return render(request,"UI/runline.html")
    else:
        return HttpResponseRedirect('/home')

def settingline(request):
    if request.method =="GET":
        return render(request,"UI/settingline.html")
    else:
        return HttpResponseRedirect('/home')


def  home(request):
    return render(request,"UI/home.html")
@login_required(login_url="/not/")
def notloggined(request):
    if request.method =="GET":
        return render(request, "UI/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return render(request,"UI/home.html")

def register(request):
    if request.method == "GET":
        return render(request, "UI/register.html")
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


