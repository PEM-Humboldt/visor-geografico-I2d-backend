
from rest_framework import serializers

from .models import Cars
# from .models import CarsQueries,CarsAmenazas


class carsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cars
        fields =(
            'car',
            'nombre'
        )

# el anterior ejemplo se puede eliminar y asi es como deberia quedar:
# como debe quedar la estructura
# class carsQueriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= CarsQueries
#         fields =(
#             'tipo',
#             'registers',
#             'species',
#             'exoticas',
#             'endemicas'
#         )

# class carsDangerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= CarsAmenazas
#         fields =(
#             'codigo',
#             'tipo',
#             'amenazadas',
#             'nombre'
#         )
