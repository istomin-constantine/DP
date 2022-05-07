from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^ajax/$', views.testspeed),
    path('statistics', views.statistics, name = 'statistics')    
]