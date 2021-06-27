# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 18 de ejercicios de pagina web

"""EJEMPLO 18:

Leer tres números enteros diferentes entre
sí y determinar el número mayor de los tres."""

class Tarea18:
    def __init__(self):
        pass
    def Factorial(self):
        print("_______________________________")
        numero=int(input("Ingrese numero: "))
        acu=1
        for num in range(numero,1,-1):
            acu =acu*num
        print("_______________________________")
        print("numero:  {}  ,Factorial:  {} ".format(numero,acu))

        print("_______________________________")
        input("enter para salir")

tarea=Tarea18()
tarea.Factorial()