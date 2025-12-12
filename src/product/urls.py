from django.urls import path
from .views import scrape_view

urlpatterns = [
    path("scrapear/", scrape_view, name="scrapear"),
]
