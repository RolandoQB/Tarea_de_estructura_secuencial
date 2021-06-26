# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 4 de ejercicios de pagina web

"""EJEMPLO 4
   Construir un algoritmo tal, que dado como dato la 
   calificación de un alumno en un examen, escriba"""

class Tarea4:
    def __init__(self):
        pass
    def Calificacion(self):
        print("_______________________________________")
        cal=float(input("Ingrese su calificacion:"))
        if cal >= 7 :
            print()
            print("!!!!!!Felicidades!!!!!!")
            print("       APROBADO")
        print()
        print("_______________________________________")
        input("enter para salir")
tarea = Tarea4()
tarea.Calificacion()