from rest_framework import serializers
from .models import Scheduling, Procedure, Patient
import datetime


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'url', 'name')


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ('id', 'url', 'name')


class SchedulingSerializer(serializers.ModelSerializer):
    initial_time = serializers.TimeField()
    final_time = serializers.TimeField()

    class Meta:
        model = Scheduling
        fields = ('id', 'date', 'initial_time', 'final_time', 'patient', 'procedure')
