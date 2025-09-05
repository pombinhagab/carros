from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class carsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('modelCar')
        userSearch = self.request.GET.get("search")
        if userSearch:
            cars = cars.filter(modelCar__icontains=userSearch)
        return cars
    
class carDetailView(DetailView):
    model = Car
    template_name = 'carDetail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class newCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'newCar.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class carUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'carUpdate.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'),name='dispatch')
class carDeleteView(DeleteView):
    model = Car
    template_name = 'carDelete.html'
    success_url = '/cars/'
