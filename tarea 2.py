# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 2 de ejercicios de pagina web

def run():
    print("_______________________________________")
    TC=float(input("Ingrese total de la compra:"))
    D=TC*0.15
    CP=TC-D
    print()
    print("Su cantidad a pagar es: ")
    print(CP)
    print("_______________________________________")
    input("enter para salir")


if __name__ == "__main__":
    run()