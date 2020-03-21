from django.shortcuts import render, HttpResponse
import requests
import json

from covid.api import CovId19Data
# Create your views here.

def index(request):
    api = CovId19Data(force=True)

    complete_data = api.get_stats()
    all_country_data = api.get_all_records_by_country()

    india_data = api.filter_by_country("india")

    #for key, value in india_data.items():
    #    if key == 'confirmed':
    #        print(value)

    #print(res)

    context = {
        'complete_data': complete_data,
        'all_country_data': all_country_data,
        'india_data': india_data
    }

    return render(request, 'stats/index.html', context)
