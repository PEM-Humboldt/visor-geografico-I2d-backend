from django.db import models

# Create your models here.

class Cars(models.Model):
    gid = models.AutoField(primary_key=True)
    car = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cars'


# el anterior ejemplo se puede eliminar y asi es como deberia quedar:
# class CarsQueries(models.Model):
#     codigo = models.CharField(max_length=5, blank=True, null=True)
#     tipo = models.TextField(blank=True, null=True)
#     registers = models.BigIntegerField(blank=True, null=True)    
#     species = models.BigIntegerField(blank=True, null=True) 
#     exoticas = models.BigIntegerField(blank=True, null=True)
#     endemicas = models.BigIntegerField(blank=True, null=True)
#     geom = models.TextField(blank=True, null=True)  # This field type is a guess.          
#     nombre = models.CharField(max_length=254, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cars_queries'


# class CarsAmenazas(models.Model):
#     codigo = models.CharField(max_length=5, blank=True, null=True)
#     tipo = models.CharField(max_length=1, blank=True, null=True)
#     amenazadas = models.BigIntegerField(blank=True, null=True)
#     geom = models.TextField(blank=True, null=True)
#     nombre = models.CharField(max_length=254, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cars_amenazas'