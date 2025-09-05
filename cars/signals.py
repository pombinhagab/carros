from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from mistralai_api.client import get_car_ai_bio



def CarInventoryUpdate():
    carsCount = Car.objects.all().count() # SELECT * FROM CARS
    carsValue = Car.objects.aggregate(
        totalValue = Sum('valueCar') # {'totalValue': 100.000}
    )['totalValue']
    CarInventory.objects.create(
        carsCount = carsCount,
        carsValue = carsValue,
    )

@receiver(pre_save, sender=Car)
def carPreSave(sender, instance, **kwargs):
    if not instance.bioCar:
        ai_bio = get_car_ai_bio(
            instance.modelCar, instance.brandCar, instance.factoryYear
        )
        instance.bioCar = ai_bio

@receiver(post_save, sender=Car)
def carPostSave(sender, instance, **kwargs):
    CarInventoryUpdate()


@receiver(post_delete, sender=Car)
def carPostDelete(sender, instance, **kwargs):
    CarInventoryUpdate()
