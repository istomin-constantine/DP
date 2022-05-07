from http import client
from threading import Thread
from urllib import response

import requests
import speedtest
from django.http import HttpResponse as hres
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


def testspeed(request):
    if request.method == 'GET':
        test  = speedtest.Speedtest()
        dl = test.download()
        up = test.upload()

        response = {
            'dl': format(dl / 1024 / 1024, ".2f"),
            'up': format(up / 1024 / 1024, ".2f"),
        }
        return JsonResponse(response)

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def index(request):
    client_addr = get_ip()

    response = requests.get(f'https://ipapi.co/{client_addr}/json/').json()
        
    data = {
        'ip': client_addr,
        'protocol': response.get("version"),
        'city': response.get("city"),
        'country_name': response.get("country_name"),
        'asn': response.get("asn"),
        'org': response.get("org"),
        'latitude': response.get("latitude"),
        'longitude': response.get("longitude"),
    }
    return render(request, 'reguser/index.html',data)

def statistics(request):
    return render(request, 'reguser/statistics.html')

