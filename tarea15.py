# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 15 de ejercicios de pagina web

"""Ejercicio 15

Diseñe un pseudocódigo para calcular la suma y producto de 
N números enteros, utilizando un bucle controlado por centinela."""

class Tarea15:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________")

        prod=1
        suma=0
        num=int(input("ingrese un numero entero que no sea negativo: "))
        print("_______________________________________")
        while num != -1 :
            
            num=int(input("Ingrese un numero: "))
            
            suma=suma+num
            prod=prod*num
            
            print("_______________________________________")
        print("""Total de la suma es:""",suma,"""
Total del producto es: """,prod)
          
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea15()
resultado.Variables()