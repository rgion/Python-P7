#P7 E13 - rgion
#Escribe un programa que le pida al usuario si quiere calcular
#si un número es primo con for o con while, por tanto, habrán
#dos funciones que se caracterizan por hacer ese mismo cálculo
#de una manera (con for y sin breaks), o de otra (con while).
#Ambas funciones devolverá true (si es es primo) o false (si
#no es primo). El programa principal informará del resultado.
#Además, como mejora puedes calcular el tiempo que tarda en
#encontrar la solución de una manera u otra. Comentario: aprovecha
#el código que tienes ya creado

from time import time

def primofor(numero):
    
    resto=1
    for i in range(numero):
        if ((i!=0)and(i!=1)and(numero%i==0)):
            resto=0
    if (resto==0):
        return False
    else:
        return True

def primowhile(numero):
    
    resto=1
    mod=1
    while(resto!=0):
        mod+=1
        resto=numero%mod
    if (mod==numero):
        return True
    else:
        return False

numero=int(input("Dame un número: "))
start=time()
print(primofor(numero))
end=time()-start
print("El for tarda: %.10f segundos." %end)
start=time()
print(primowhile(numero))
end=time()-start
print("El while tarda: %.10f segundos." %end)

