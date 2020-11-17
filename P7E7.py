#P7 E7 - rgion
#Escribe un programa que lea una frase, y la pase como
#parámetro a un procedimiento. El procedimiento contará
#el número de vocales (de cada una) que aparecen, y lo
#imprimirá por pantalla.
def cadena(nombre):
    a=0
    e=0
    i=0
    o=0
    u=0
    for k in range(len(nombre)):
        if (nombre[k]=="a"):
            a+=1
        if (nombre[k]=="e"):
            e+=1
        if (nombre[k]=="i"):
            i+=1
        if (nombre[k]=="o"):
            o+=1
        if (nombre[k]=="u"):
            u+=1
    print("a=",a,"e=",e,"i=",i,"o=",o,"u=",u)

nombre=input("Dime un nombre: ")
cadena(nombre)
