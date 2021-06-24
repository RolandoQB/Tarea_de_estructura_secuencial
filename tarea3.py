# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Tarea 2 de ejercicios de pagina web

def run():
    print("_______________________________________")
    SB=float(input("Ingrese Salario Base:"))
    V1=float(input("Ingrese valor de venta 1:"))
    V2=float(input("Ingrese valor de venta 2:"))
    V3=float(input("Ingrese valor de venta 3:"))
    TV=V1+V2+V3
    C=TV*0.1
    TR=SB+C
    print()
    print("Su Total a Recibir es: ")
    print("$",TR)
    print("_______________________________________")
    input("enter para salir")


if __name__ == "__main__":
    run()