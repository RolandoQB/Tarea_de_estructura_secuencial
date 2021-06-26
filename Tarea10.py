# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 10 de ejercicios de pagina web

"""Ejercicio 10

Un ejemplo en el cual usamos el operador lógico AND sería:

Una escuela aplica dos exámenes a sus aspirantes, por lo que 
cada uno de ellos obtiene dos calificaciones denotadas como 
C1 y C2. El aspirante que obtenga calificaciones mayores que 
80 en ambos exámenes es aceptado; en caso contrario es rechazado."""

class Tarea10:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________")
        C1= float(input("Ingrese primer Calificacion: "))
        C2= float(input("Ingrese segunda Calificacion: "))
        print("_______________________________________")
        if C1>=80 and C2>= 80:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("             ACEPTADO",)
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("              RECHAZADO")
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea10()
resultado.Variables()