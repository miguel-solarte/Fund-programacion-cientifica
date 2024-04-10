from django.contrib import admin
from django.urls import path
from KPI.views import kpi, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kpi/', kpi),
    path('buscar/', buscar),
]
