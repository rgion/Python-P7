#P7 E2 - rgion
#Escribe un programa que lea el nombre y los dos apellidos
#de una persona (en tres cadenas de caracteres diferentes),
#los pase como parámetros a una función, y ésta debe unirlos
#y devolver una única cadena. La cadena final la imprimirá
#el programa por pantalla.
def cadena(lista):
    completo=lista[0]
    for i in range(1,len(lista)):
        completo+=" "+lista[i]
    return completo

lista=[]
nombre=input("Introduce el nombre: ")
lista.append(nombre)
apellido1=input("Introduce el primer apellido: ")
lista.append(apellido1)
apellido2=input("Introduce el segundo apellido: ")
lista.append(apellido2)
print(cadena(lista))
