"""
Programa que convierte binario de 8 bits a decimal y viceversa.
Autores: Juan Salguero, Santiago Cordero, Diego Gudiel
"""
import os

def binario_a_decimal(binario:str):
    decimal = 0
    for i in range(8):
        if (binario[i] != "0"):
            decimal += 2**(7-i) # Suma la potencia de 2 correspondiente a la casilla del número binario, siendo 2^7 la más alta que puede representar.
    return decimal


def decimal_a_binario(decimal:int):
    residuo = 1
    binaryString = ""
    while (residuo != 0):
        residuo = decimal % 2
        decimal = decimal // 2
        if (residuo != 0):
            binaryString = str(residuo) + binaryString
    if (len(binaryString) != 8):
        binaryString = "0"*(8-len(binaryString)) + binaryString
    return binaryString

def isNumber(string:str):
    try:
        int(string)
        return True
    except ValueError:
        return False

loop = True
menu = "------------------" + "\n Programa convertor de binario-decimal o decimal-binario\n" + "--------------------" + "\nOpciones disponibles: \n 1. Convertir un binario a decimal\n 2. Convertir un decimal a binario\n 3. Salir del programa\n"
os.system("cls")
while loop:
    print(menu)
    opcion = input("Ingrese el número de la opción deseada: ")
    match(opcion):
        case "1":
            binario = str(input("Ingrese el binario a convertir (de 8 bits exactos, sin espacios): "))
            if (len(binario) != 8 or binario.__contains__(" ") or not isNumber(binario)):
                while True:
                    print("Debe de ingresar un número binario válido, intente otra vez.")
                    binario = str(input("Ingrese el binario a convertir (de 8 bits exactos, sin espacios): "))
                    if (len(binario) == 8 and (not binario.__contains__(" ")) and isNumber(binario)):
                        break
            print(f"El número {binario} en decimal representa {binario_a_decimal(binario)}")
        case "2":
            decimal = input("Ingrese el número entero a convertir (positivo menor que 256): ")
            if (isNumber(decimal)):
                if (int(decimal) < 256):
                    print(f"El decimal {decimal} en sistema binario es {decimal_a_binario(int(decimal))}")
            else:
                while True:
                    print("Ingrese un número válido.")
                    decimal = input("Ingrese el número entero a convertir (positivo menor que 256): ")
                    if (isNumber(decimal)):
                        if (int(decimal) < 256):
                            break
        case "3":
            loop = False
            print("Gracias por usar nuestro programa. :D")
        case _:
            print("Opción no válida. Intente nuevamente.")
    input("Ingrese cualquier tecla para continuar...")
    os.system("cls")
