from django.contrib import admin
from .models import Scheduling, Patient, Procedure

# Register your models here.
admin.site.register(Scheduling)
admin.site.register(Patient)
admin.site.register(Procedure)
