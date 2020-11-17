#P7 E6 - rgion
#Escribe un programa que lea el nombre de una persona y un
#carácter, le pase estos datos a una función que comprobará
#si dicho carácter está en su nombre. El resultado de dicha
#función lo imprimirá el programa principal por pantalla.
def cadena(nombre,caracter):
    for i in range(len(nombre)):
        if (nombre[i]==caracter):
            return "El carácter está en el nombre"

nombre=input("Dime un nombre: ")
caracter=input("Dime un carácter: ")
print(cadena(nombre,caracter))
