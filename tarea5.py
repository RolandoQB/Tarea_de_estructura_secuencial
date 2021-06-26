# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 5 de ejercicios de pagina web

"""EJEMPLO 5:
 Dado como dato la calificación de un alumno en un examen, 
 escriba “aprobado” si su calificación es mayor o igual que 7 
 y “Reprobado” en caso contrario."""

class Tarea5:
    def __init__(self):
        pass
    def Calcular(self):
        print("_______________________________________")
        cal=float(input("Ingrese su calificacion:"))
        if cal >= 7 :
            print()
            print("!!!!!!Felicidades!!!!!!")
            print("       APROBADO")
        else:
            print()
            print("!!!!!!Ho no, esfuerzate mas!!!!!!")
            print("          REPROBADO")
        print()
        print("_______________________________________")
        input("enter para salir")

tarea = Tarea5()
tarea.Calcular()