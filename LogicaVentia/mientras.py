# Importar librerias / Recetas y codigos prefabricados 
import math




#Variable controladora
opcion = 1

while(opcion!=0):
    #declaro el bucle/muchos adjetivos / la vuelta :3
    print("Empanadas de 100 y 200")
    print("*****")
    print("0. Digita 0 para salir")
    print("1. Digita 1 para calcular la raiz cuadrada de un numero")
    print("2. Digita 2 para calcular la potencia 2 de un numero")
    print("*****")
    #pregunte por la opcion
    opcion = int(input("Digita una opcion"))

    if(opcion ==0):
        break
    elif(opcion==1):
        numero=int(input("Digita un numero: "))
        raiz=math.sqrt(numero)
        print(f"La raiz de {numero} es: {raiz}")
    elif(opcion==2):
        numero=int(input("Digita un numero: "))
        potencia=math.pow(numero,2)
        print(f"La potencia de {numero} es: {potencia}")
    else:
        print("Numero ingresado no es valido")
        