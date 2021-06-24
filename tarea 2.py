# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 2 de ejercicios de pagina web

"""EJEMPLO 2:
En una tienda se ofrece un descuento del 15% sobre el 
total de la compra y un cliente desea saber cuánto deberá 
pagar finalmente por su compra."""

def run():
    print("_______________________________________")
    TC=float(input("Ingrese total de la compra:"))
    D=TC*0.15
    CP=TC-D
    print()
    print("Su cantidad a pagar es: ")
    print("$",CP)
    print("_______________________________________")
    input("enter para salir")


if __name__ == "__main__":
    run()