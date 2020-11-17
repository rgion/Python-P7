#P7 E9 - rgion
#Escribe un programa que pida dos palabras las pase como
#parámetro a un procedimiento y diga si riman o no. Si
#coinciden las tres últimas letras tiene que decir que riman.
#Si coinciden sólo las dos últimas tiene que decir que riman
#un poco y si no, que no riman.

def cadena(palabra1,palabra2):
    if palabra1[-3:]==palabra2[-3:]:
        print("Las palabras",palabra1,"y",palabra2,"riman.")
    elif palabra1[-2:]==palabra2[-2:]:
        print("Las palabras",palabra1,"y",palabra2,"riman un poco.")
    else:
        print("Las palabras",palabra1,"y",palabra2,"no riman.")

palabra1=input("Dime una palabra: ")
palabra2=input("Dime otra palabra: ")
cadena(palabra1,palabra2)
