# Ex02 Django ORM Web Application
## Date: 18/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM)
 
## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
admin.py
from django.contrib import admin
from.models import footballplayers,footballplayersAdmin
admin.site.register(footballplayers,footballplayersAdmin)

models.py
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


```


## OUTPUT

![Alt text](<Screenshot 2023-10-18 090949.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
