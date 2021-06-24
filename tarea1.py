# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 1 de ejercicios de pagina web

"""EJEMPLO 1.
En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la 
superficie de un círculo para un radio cualquiera.
El Flujograma que representa a dicho ejemplo es el siguiente:"""

def run():
    # escribir el codigo
    pi=3.1416
    superficie = int(input("Ingrese el diametro del circulo : "))
    print("_______________________________________")
    area = pi * superficie/2*100
    print("La superficie del circulo es: ")
    print(area)
    print("_______________________________________")

    input("enter para salir")

if __name__ == "__main__":
    run()