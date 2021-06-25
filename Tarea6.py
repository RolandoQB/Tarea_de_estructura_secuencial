# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 6 de ejercicios de pagina web

"""EJEMPLO 6:

Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento 
del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento."""

def run():
    print("_______________________________________")
    SUELDO=float(input("Sueldo de empleados:"))
    if SUELDO < 600:
        NS=SUELDO + SUELDO*0.1
        print()
    else:
        NS=SUELDO
        print()
    print("_______________________________________")    
    print(NS)
    print("_______________________________________")
    input("enter para salir")

if __name__ == "__main__":
    run()