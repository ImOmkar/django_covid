from django.shortcuts import render, HttpResponse
import requests
import json

from covid import Covid
# Create your views here.

def index(request):
    covid = Covid()

   # data = covid.get_data()

    india_cases = covid.get_status_by_country_name("India")

    confirmed = covid.get_total_confirmed_cases()

    recovered = covid.get_total_recovered()

    deaths = covid.get_total_deaths()

    active = covid.get_total_active_cases()

    print(confirmed, recovered, deaths, active)


    context = {
       # 'data': data,
        'india_cases': india_cases,
        'confirmed': confirmed,
        'deaths': deaths,
        'active': active,
        'recovered': recovered,
    }

    return render(request, 'stats/covid.html', context)
