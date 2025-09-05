from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import carsListView, newCarCreateView, carDetailView, carUpdateView, carDeleteView
from accounts.views import registerView, loginView, logoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('cars/', carsListView.as_view(), name='cars_list'),
    path('newCar/', newCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', carDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', carUpdateView.as_view(), name='car_update'),
     path('car/<int:pk>/delete/', carDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
