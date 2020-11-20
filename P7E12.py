#P7 E12 - rgion
#Escribir un programa que lea una frase, y pase ésta como
#parámetro a una función que debe contar el número de palabras
#que contiene. Debe imprimir el programa principal el resultado.
# a)Asumir que cada palabra está separada por un solo blanco:
# b)No se sabe cómo están separadas las palabras. Pueden estar
#   separadas por más de un blanco o por signos de puntuación.


def cadena(string):
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    signos=[".",":",",",";","-"]
    palabras=0
    for i in range(len(string)):
        if string[i]==" " and (string[i-1] in signos or string[i-1] in letras):
            palabras+=1
    if len(string)!=0:#si nos han introducido texto es que al menos tenemos una palabra
        palabras +=1  # y la última palabra no tiene espacio ya que le damos al retorno de carro

    return palabras

string=input("Introduce una frase: ")
print("La frase contiene",cadena(string),"palabras.")
