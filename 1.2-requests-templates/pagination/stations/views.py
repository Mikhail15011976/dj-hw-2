from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = []
        for row in reader:
            bus_stations.append(row)
        page_number = int(request.GET.get("page", 5))
        paginator = Paginator(bus_stations, 2)
        page = paginator.get_page(page_number)


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
