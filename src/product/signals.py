from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.db.models.signals import post_migrate
from django.dispatch import receiver

import json


@receiver(post_migrate)
def create_scrape_product_data_task(sender, **kwargs):

    # Crea la tarea periódica solo en la actual app (product).
    if sender.name != "product":
        return

    # Crear u obtener intervalo de 1 hora.
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.HOURS,
    )

    # Crear la tarea si no existe.
    PeriodicTask.objects.get_or_create(
        name="Scraping con 1 hora de intervalo",
        task="scrape_and_export",
        interval=schedule,
        defaults={
            "kwargs": json.dumps({}),
        }
    )
