from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=500, null=True)
    asin = models.CharField(max_length=50, null=True)
    thumbnail = models.URLField(null=True)
    price = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=20, null=True)
    reviews = models.CharField(max_length=20, null=True)
    link = models.URLField(null=True)

    screaped_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Escrapeado el")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['screaped_at']

    def __str__(self):
        return self.title or "Producto sin título"
