# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 12 de ejercicios de pagina web

"""Ejercicio 12

Calcular la suma de los cuadrados de los primeros 
100 enteros y escribir el resultado."""

class Tarea12:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________")
    i=1
    suma=0
    x=range(100)
    for i in x:
        suma=suma+i*i
        print("Suma: ",suma)

resultado = Tarea12()
resultado.Variables()
        
