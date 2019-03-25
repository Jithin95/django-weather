from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length = 25)

    class Meta:
        verbose_name_plural = "cities"
