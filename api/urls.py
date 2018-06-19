from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('scheduling', views.SchedulingView)
router.register('procedure', views.ProcedureView)
router.register('patient', views.PatientView)

urlpatterns = [
    path('', include(router.urls))
]
