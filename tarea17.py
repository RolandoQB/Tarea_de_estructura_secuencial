# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 17 de ejercicios de pagina web

"""Ejercicio 17

Aplicar los pasos de la metodología para la solución de un 
problema para leer un número entero N y calcular el resultado 
de la siguiente serie:."""

class Tarea17:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________") 
        l=1
        n=int(input("ingrese un numero para la serie: "))
        print("_______________________________________") 
        s=5
        ser=0
        for a in range(l,n+1):
            s=s+5
            ser=ser+s
        print("la suma de la serie es:", ser)

                  
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea17()
resultado.Variables()