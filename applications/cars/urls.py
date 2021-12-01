from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/cars/carsAll', views.Cars.as_view())

    # el anterior ejemplo se puede eliminar y asi es como deberia quedar:
    # path('api/cars/charts/<kid>', views.carsQuery.as_view()),
    # path('api/cars/dangerCharts/<kid>', views.carsDanger.as_view())

]
