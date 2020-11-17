#P7 E8 - rgion
#Escribe un programa que pida una frase, y pase la frase
#como parámetro a una función que debe eliminar los espacios
#en blanco (compactar la frase). El programa principal imprimirá
#por pantalla el resultado final.

def cadena(frase):
    
    for i in range(len(frase)):
        if frase[i]==" ":
            frase1=frase.replace(frase[i],"")
    return frase1

frase=input("Dime una frase: ")
print(cadena(frase))
