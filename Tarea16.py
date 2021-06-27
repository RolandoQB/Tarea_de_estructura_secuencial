# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 16 de ejercicios de pagina web

"""Ejercicio 16

Determinar si un número entero proporcionado por 
el usuario es primo. Un número primo es un entero 
que no tiene más divisores que él mismo y la unidad."""

class Tarea16:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________") 
        primo= 0
        divisor=2
        num=int(input("ingrese un numero entero : "))
        print("_______________________________________")
        
        while divisor < num and primo ==0 :
            Res= num%divisor
            print(Res)
            if Res == 0:
                primo+=1
            divisor+=1
        if primo ==0:
            print("Numero",num,"es primo")
        else:
            print("Numero",num,"no es primo")
                       
            print("_______________________________________")
                  
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea16()
resultado.Variables()