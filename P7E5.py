#P7 E5 - rgion
#Escribe un programa que te pida una frase y una vocal,
#y pase estos datos como parámetro a una función que se
#encargará de cambiar todas las vocales de la frase por
#la vocal seleccionada. Devolverá la función la frase
#modificada, y el programa principal la imprimirá:
def cadena(frase,vocal):
    lista=["a","e","i","o","u"]
    for i in range(len(frase)):
        if frase[i] in lista:
            frase=frase[:i]+vocal+frase[(i+1):]
    return frase

frase=input("Dime algo: ")
vocal=input("Dime una vocal: ")
print(cadena(frase,vocal))