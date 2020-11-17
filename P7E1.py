#P7 E1 - rgion
#Escribe un programa que pida un texto por pantalla, este
#texto lo pase como parámetro a un procedimiento, y éste lo
#imprima primero todo en minúsculas y luego todo en mayúsculas.
def texto(cadena):
    print(cadena.lower())
    print(cadena.upper())

cadena=input("Introduce un texto: ")
texto(cadena)
