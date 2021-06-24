# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 1 de ejercicios de pagina web

"""EJEMPLO 1.
En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la 
superficie de un círculo para un radio cualquiera.
El Flujograma que representa a dicho ejemplo es el siguiente:"""

def run():
    pi=3.1416
    R =int(input("Ingrese el Radio del circulo : "))
    print("_______________________________________")
    cal =R*R
    S=cal*pi
    print("La superficie del circulo es: ")
    print(S)
    print("_______________________________________")

    input("enter para salir")

if __name__ == "__main__":
    run()