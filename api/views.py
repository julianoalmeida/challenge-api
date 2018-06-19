from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Procedure, Scheduling
from .serializers import PatientSerializer, ProcedureSerializer, SchedulingSerializer


class PatientView(viewsets.ModelViewSet):
    """
    API endpoint that allows patient to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ProcedureView(viewsets.ModelViewSet):
    """
    API endpoint that allows procedure to be viewed or edited.
    """
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class SchedulingView(viewsets.ModelViewSet):
    """
    API endpoint that allows scheduling to be viewed or edited.
    """
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
