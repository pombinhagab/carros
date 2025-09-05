from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    idBrand = models.AutoField(primary_key=True)
    nameBrand = models.CharField(max_length=200)

    def __str__(self):
        return self.nameBrand


class Car(models.Model):
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('seminovo', 'Seminovo'),
        ('usado', 'Usado'),
    ]
    idCar = models.AutoField(primary_key=True)
    modelCar = models.CharField(max_length=200)
    brandCar = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="carBrand")
    factoryYear = models.IntegerField(blank=True, null=True)
    modelYear = models.IntegerField(blank=True, null=True)
    plateCar = models.CharField(max_length=10, blank=True, null=True)
    valueCar = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    carOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ownerCar", null=True)
    carStatus = models.CharField(max_length=10, choices=STATUS_CHOICES, default='novo')
    bioCar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.modelCar
    

class CarInventory(models.Model):
    carsCount = models.IntegerField()
    carsValue = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return f'{self.carsCount} - {self.carsValue}'