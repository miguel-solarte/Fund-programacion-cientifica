from django.db import models

# Create your models here.

class Asociados(models.Model):
    nombre = models.CharField(max_length = 50)
    hr_trab = models.IntegerField() #horas trabajadas
    can_prod_ven = models.IntegerField() #cantidad productos vendidos
    can_din_total = models.IntegerField() #cantidad de dinero total

