import requests

from helpers import config
from celery import shared_task
from .models import Product


@shared_task
def scrape_product_data():
    SERPAPI_API_KEY = config("SERPAPI_API_KEY")

    keywords = [
        "xbox series x",
        "xbox series s",
        "playstation 5",
        "mac",
        "apple watch",
        "asus rog",
    ]

    params = {
        "api_key": SERPAPI_API_KEY,
        "engine": "amazon",
        "k": keywords,
        "s": "price-desc-rank",
        "amazon_domain": "amazon.es",
    }

    response = requests.get("https://serpapi.com/search", params=params).json()

    for result in response.get("organic_results", []):
        Product.objects.create(
            title=result.get("title"),
            asin=result.get("asin"),
            thumbnail=result.get("thumbnail"),
            price=result.get("price"),
            rating=result.get("rating"),
            reviews=result.get("reviews"),
            link=result.get("link"),
        )

    return "Scraping completado."


@shared_task
def create_csv_task(_=None):
    import csv
    import os

    # Ruta en local para guardar el CSV.
    export_dir = "/exports_local"
    os.makedirs(export_dir, exist_ok=True)

    csv_path = os.path.join(export_dir, 'productos_exportados.csv')

    with open(csv_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["title", "asin", "thumbnail",
                        "price", "rating", "reviews", "link"])

        for p in Product.objects.all():
            writer.writerow([
                p.title,
                p.asin,
                p.thumbnail,
                p.price,
                p.rating,
                p.reviews,
                p.link,
            ])

    return f"CSV creado correctamente en {csv_path}."


@shared_task
def scrape_and_export():
    from celery import chain
    return chain(
        scrape_product_data.s(),
        create_csv_task.s()
    )()
