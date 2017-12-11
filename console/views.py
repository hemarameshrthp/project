from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UI.models import MachineStatus


@login_required(login_url="/not/")
def console(request):
    ms = MachineStatus.objects.all()
    return render(request, "console/index.html", {"data": ms})