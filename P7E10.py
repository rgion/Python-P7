#P7 E10 - rgion
#Escribe un programa que te pida una palabra o número,
#pase por parámetro estos datos a una función, y ésta
#te diga si es o no palíndroma o capicúa. El programa
#principal imprimirá el resultado de la función

def cadena(string):
    igual=0
    aux=0
    for ind in reversed(range(0, len(string))):
      if string[ind].lower()==string[aux].lower():
        igual+=1
      aux+=1
    if len(string)==igual:
      return "El texto es palindromo!"
    else:
      return "El texto no es palindromo!"
      
string=input("Introduce una palabra o número: ")
print(cadena(string))
