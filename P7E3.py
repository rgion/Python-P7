#P7 E3 - rgion
#Escribe un programa que lea una frase, y la pase como
#parámetro a un procedimiento, y éste debe mostrar la frase
#con un carácter en cada línea.
def cadena(frase):
    for i in range(len(frase)):
        print(frase[i])

frase=input("Introduce una frase: ")
cadena(frase)
