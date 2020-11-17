#P7 E4 - rgion
#Escribe un programa que pida una frase, y le pase como
#parámetro a una función dicha frase. La función debe sustituir
#todos los espacios en blanco de una frase por un asterisco, y devolver
#el resultado para que el programa principal la imprima por pantalla.
def cadena(frase):
    for i in range(len(frase)):
        if frase[i]==" ":
            frase=frase[:i]+"*"+frase[(i+1):]
    return frase

frase=input("Introduce una frase: ")
print(cadena(frase))
