from http import client
from django.shortcuts import render

from django.http import HttpResponse as hres
from django.views import View

def index(request):
    #client_addr = request.META.get('REMOTE_ADDR')
    return hres("hello world")