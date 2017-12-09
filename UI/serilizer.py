from  .models import MachineStatus,Idle,Run,Setting
from rest_framework import serializers


class MachineStatusSer(serializers.ModelSerializer):
    class Meta:
        model = MachineStatus
        fields = ("status", "date")

class IdleSer(serializers.ModelSerializer):
    class Meta:
        model= Idle
        fields= {"idle_diff","idle_start","idle_stop","date"}

class RunSer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ("run_diff","run_start","run_stop","date1")

class SettingSer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ("sett_diff","sett_start","sett_stop","date2")