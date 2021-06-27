# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 14 de ejercicios de pagina web

"""Ejercicio 14

Diseñe un pseudocódigo para calcular
la suma y producto de N números enteros, 
utilizando un bucle controlado por el usuario.."""

class Tarea14:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________")

        prod=1
        suma=0
        resp=input(str("Quieres ingresar numeros??  (S/N)"))
        print("_______________________________________")
        while resp != "n" and resp!= "N":
            
            num=int(input("Ingrese un numero: "))
            print("_______________________________________")
            suma=suma+num
            prod=prod*num
            resp=input(str("Desea continuar (S/N)"))
            print("_______________________________________")
        print("""Total de la suma es:""",suma,"""
Total del producto es: """,prod)
          
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea14()
resultado.Variables()