from django.db import models

# Create your models here.
class MachineStatus(models.Model):
    status = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    # def __str__(self):
    #     return  str(self.status)
    class Meta:
        db_table = "MachineStatus"

class Idle(models.Model):

    idle_start=models.TimeField()
    idle_stop=models.TimeField()
    idle_diff=models.TimeField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.id + " " + str(self.idle_diff) + " " + str(self.idle_start) + " " + str(self.idle_stop) + " " + str(self.date)
    class Meta:
        db_table ="Idle"

class Run(models.Model):
    run_start = models.TimeField()
    run_stop = models.TimeField()
    run_diff = models.TimeField()
    date1 = models.DateField(auto_now=True)

    def __str__(self):
        return self.id + " " + str(self.run_diff) + " " + str(self.run_start) + " " + str(self.run_stop) + " " + str(self.date1)
    class Meta:
        db_table ="Run"


class Setting(models.Model):
    sett_start = models.TimeField()
    sett_stop = models.TimeField()
    sett_diff = models.TimeField()
    date2 = models.DateField(auto_now=True)

    def __str__(self):
        return self.id + " " + str(self.sett_diff) + " " + str(self.sett_start) + " " + str(self.sett_stop) + " " + str(self.date2)
    class Meta:
        db_table = "Setting"

class DailyProgress(models.Model):
    date = models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    parts=models.IntegerField(default=0)
    manufacturingtime=models.TimeField()
    idletime=models.IntegerField()
    runtime=models.IntegerField()
    settingtime=models.IntegerField()

    def __str__(self):
        return self.id + " " + str(self.date) + " " + str(self.time) + " " + str(self.parts) + " " +str(self.manufacturingtime) + " " +str(self.idletime) + " " +str(self.runtime) + " " +str(self.settingtime)

