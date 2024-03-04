from django.db import models
from django.urls import reverse
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 200, help_text = "Enter the city name")
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null = True)
    tempValue = models.DecimalField(help_text = "Enter the temperature", max_digits = 3, decimal_places=1)
    dateTempUpdate = models.DateTimeField(help_text="Enter the date of temp update")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('city_detail', args=[str(self.id)])


class Country(models.Model):
    name = models.CharField(max_length = 200, help_text = "Enter the country name")
    def __str__(self):
        return self.name