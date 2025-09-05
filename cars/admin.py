from django.contrib import admin
from cars.models import Car, Brand



class CarAdmin(admin.ModelAdmin):
    list_display = ("modelCar", "brandCar", "factoryYear", "modelYear", "valueCar", "plateCar", "carOwner")
    search_fields = ("modelCar","brandCar",)

class BrandAdmin(admin.ModelAdmin):
    list_display = ("idBrand", "nameBrand",)
    search_fields = ("nameBrand",)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)