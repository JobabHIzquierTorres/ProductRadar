from django.shortcuts import render
from django.http import JsonResponse
from .tasks import scrape_product_data

# Create your views here.


def scrape_view(request):
    scrape_product_data.delay()
    return JsonResponse({"status": "Scraping iniciado"})
