import secrets
from datetime import date, datetime, timedelta
from http import client
from lib2to3.pgen2 import token
from threading import Thread
from urllib import response

import matplotlib.pyplot as plt
import numpy as np
import requests
from django.http import HttpResponse as hres
from django.http import JsonResponse, request
from django.shortcuts import render
from django.views import View

from .models import visitors


def add_record(info):
    visit = visitors()
    visit.ipField = info["ip"]
    visit.protocolField = info["protocol"]
    visit.countryField = info["country_name"]
    visit.cityField = info["city"]
    visit.providerField = info["org"]
    visit.cookie = info["cookie"]
    current_time = datetime.now()
    current_date = date.today()
    visit.date = current_date.strftime("%d/%m/%Y")
    visit.time = datetime.now().strftime('%H:%M:%S')
    if not visitors.objects.all() and visit.countryField is not None:
        visit.save()
    else:
        for i in reversed(visitors.objects.all()):
            if i.cookie == visit.cookie and datetime.strptime(visit.time, '%H:%M:%S') - datetime.strptime(i.time, '%H:%M:%S') > timedelta(minutes=10) and visit.countryField is not None:
                print('hello1')
                visit.save()
                break
            elif i.cookie == visit.cookie and datetime.strptime(visit.time, '%H:%M:%S') - datetime.strptime(i.time, '%H:%M:%S') < timedelta(minutes=0) and visit.countryField is not None:
                print('hello2')
                visit.save()
                break
            elif i.cookie == visit.cookie:
                print('bebra')
                break
        


def get_ip_local(request):
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_ip(request):
    return(request.META.get('REMOTE_ADDR'))
    #return(request.META.get('HTTP_X_FORWARDED_FOR'))

def index(request):
    client_addr = get_ip_local(request)

    #response = requests.get(f'https://ipapi.co/{client_addr}/json/').json()
    response = requests.get(f"http://ipwho.is/{client_addr}").json()
    print()


    if request.COOKIES.get('matrix') is None:
        cookie = secrets.token_hex(16)
    else:
        cookie = request.COOKIES.get('matrix')

    data = {
        'ip': client_addr,
        'protocol': response.get("type"),
        'city': response.get("city"),
        'country_name': response.get("country"),
        'asn': response.get('connection').get("asn"),
        'org': response.get('connection').get('org'),
        'latitude': response.get("latitude"),
        'longitude': response.get("longitude"),
        'cookie': cookie,
    }
    add_record(data)
    resp = render(request, 'reguser/index.html', data)
    if request.COOKIES.get('matrix') is None:
        resp.set_cookie('matrix', cookie)
    return resp

def statistics(request):
    visitors_output= visitors.objects.order_by('-id')[:10]
    
    ####################
    vis = visitors.objects.values_list('countryField', flat=True)
    ####################
    
    arr = ['Ukraine','Netherlands','Ukraine','Ukraine','Germany','Ukraine','Germany','Netherlands','Ukraine','France','Germany','Ukraine','France']
    values, counts =  np.unique(vis, return_counts=True)   

    plt.pie(counts,labels=values,autopct='%1.1f%%')
    plt.title('Countries')
    plt.axis('equal')
    plt.savefig('reguser/static/reguser/countries.png')


    print(values,counts)

    return render(request, 'reguser/statistics.html', {'visitors_output': visitors_output})

