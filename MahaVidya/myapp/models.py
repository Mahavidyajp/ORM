from django.db import models 
from django.contrib import admin
class footballplayers(models.Model):
    Playerid=models.CharField(max_length=15)
    Playername=models.CharField(max_length=30)
    Event=models.CharField(max_length=50)
    Category=models.CharField(max_length=20)
    Age=models.IntegerField()
class footballplayersAdmin(admin.ModelAdmin):
    list_display=["Playerid","Playername","Event","Category","Age"]
