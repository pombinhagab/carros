from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_valueCar(self):
        valueCar = self.cleaned_data.get("valueCar")
        if valueCar < 20000:
            self.add_error("valueCar", "Valor mínimo do carro deve ser de R$20.000")
        return valueCar

    def clean_factoryYear(self):
        factoryYear = self.cleaned_data.get("factoryYear")
        if factoryYear < 1975:
            self.add_error("factoryYear", "Não é possivel cadastrar carros fabricados antes de 1975")
        return factoryYear