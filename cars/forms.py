from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['carOwner']
        labels = {
            'modelCar': 'Modelo do Carro',
            'brandCar': 'Marca do Carro',
            'factoryYear': 'Ano de Fabricação (Acima de 1975)',
            'modelYear': 'Ano do Modelo (Acima de 1975)',
            'plateCar': 'Placa do Carro',
            'valueCar': 'Valor do Carro (Minimo R$20.000)',
            'photo': 'Foto do Carro',
            'bioCar': 'Descrição do Carro',
            'carStatus': 'Status do Carro',
        }

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