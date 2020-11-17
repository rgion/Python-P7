#P7 E11 - rgion
#Escribe un programa que te pida una frase, y pase la
#frase como parámetro a una función. Ésta debe devolver
#si es palíndroma o no , y el programa principal escribirá
#el resultado por pantalla:

def cadena(string):
    for i in range(len(string)):
        if string[i]==" ":
            string1=string.replace(string[i],"")
    igual=0
    aux=0
    for i in reversed(range(len(string1))):
      if string1[i].lower()==string1[aux].lower():
        igual+=1
      aux+=1
    if len(string1)==igual:
      return "La frase es un palíndromo!"
    else:
      return "La frase no es un palíndromo!"
      
string=input("Introduce una frase: ")
print(cadena(string))
