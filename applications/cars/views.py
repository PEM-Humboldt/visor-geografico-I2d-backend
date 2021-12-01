from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Cars
from .serializers import carsSerializer

# from .models import CarsQueries,CarsAmenazas
# from .serializers import carsQueriesSerializer,carsDangerSerializer

class CarsAll(ListAPIView):
    serializer_class=carsSerializer

    def get_queryset(self):
        return Cars.objects.all() 


# como debe quedar
# class carsQuery(ListAPIView):
#     serializer_class=carsQueriesSerializer

#     def get_queryset(self):
#         kid = self.kwargs['kid']
#         return CarsQueries.objects.filter(codigo=kid).exclude(tipo__isnull=True).distinct('tipo')


# class carsDanger(ListAPIView):
#     serializer_class=carsDangerSerializer

#     def get_queryset(self):
#         kid = self.kwargs['kid']
#         return CarsAmenazas.objects.filter(codigo=kid).exclude(tipo__isnull=True)

