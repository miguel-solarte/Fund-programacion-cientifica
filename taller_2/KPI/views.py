from django.shortcuts import render
from django.http import HttpResponse
from KPI.models import Asociados


# Create your views here.

class KPI():
    def __init__(self):
        pass
        
    def kpi_1(self, val_1):

        return (val_1/30) * 100
    
    def kpi_2(self, val_1):

        return (val_1/20) * 100
    
    def kpi_3(self, val_1):

        return (val_1/500000) * 100
    
    def kpi_4(self, val_1, val_2):

        return (val_1/val_2)
    
    def kpi_5(self, val_1, val_2):

        return (val_1/val_2)
    
    def kpi_6(self, val_1, val_2, val_3):

        return (((val_1 / 1000) + val_2) / val_3) 
    
    def kpi_7(self, val_1, val_2, val_3):

        return (((val_1 / 1000) ** 2 + val_2) / val_3) 
    
    def kpi_8(self, val_1, val_2):

        return (val_1 / 500000) - (val_2 / 20)
    
    def kpi_9(self, val_1, val_2):

        return (val_1 / 30) - (val_2 / 20)
    
    def kpi_10(self, val_1, val_2):

        return (val_1 / (500000 * 100)) - (val_2 / 20)
    
    
def kpi(request):

    kpi1 = KPI()

    if request.GET["name_asoc"]:

        nombre_asociado = request.GET["name_asoc"]

        if len(nombre_asociado) > 20:

            mensaje = "Texto demasiado largo"
        else:

            asociado = Asociados.objects.filter(nombre__icontains = nombre_asociado)

            hr_trabajadas = asociado[0].hr_trab
            cant_produc_vendidos = asociado[0].can_prod_ven
            cant_din_total = asociado[0].can_din_total

        
            return render(request, "viewkpi.html", {"kpi1": kpi1.kpi_1(cant_produc_vendidos), 
                                                    "kpi2": kpi1.kpi_2(hr_trabajadas), 
                                                    "kpi3": kpi1.kpi_3(cant_din_total), 
                                                    "kpi4": kpi1.kpi_4(cant_produc_vendidos, hr_trabajadas), 
                                                    "kpi5": kpi1.kpi_5(cant_din_total, hr_trabajadas), 
                                                    "kpi6": kpi1.kpi_6(cant_din_total, cant_produc_vendidos, hr_trabajadas), 
                                                    "kpi7": kpi1.kpi_7(cant_din_total, cant_produc_vendidos, hr_trabajadas), 
                                                    "kpi8": kpi1.kpi_8(cant_din_total, hr_trabajadas), 
                                                    "kpi9": kpi1.kpi_9(cant_produc_vendidos, hr_trabajadas), 
                                                    "kpi10": kpi1.kpi_10(cant_din_total, hr_trabajadas)})
    
    else:

        mensaje =  "No hay texto" 

    return HttpResponse(mensaje)

    


def buscar(request):

    return render(request, "desempeñoasociado.html")
    



