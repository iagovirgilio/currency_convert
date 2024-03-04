from django.db import models


class Coin(models.Model):
    class Meta:
        verbose_name = 'Moeda'
        verbose_name_plural = 'Moedas'

    name = models.CharField(max_length=16)
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name
