#P7 E14 - rgion
#Aprovechando el potencial de los diccionarios, escribe 
#un programa que llame a un procedimiento, que recibe como
#parámetro la fecha en números y devuelve la fecha  con el
#nombre del mes. Comentario: no es necesario validar si la
#es correcta, damos por hecho que lo será.

def nombre_mes(fecha):

    dia,mes,año=fecha[:2],fecha[3:5],fecha[-4:]
    meses={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
    for k,v in meses.items():
        if mes==k:
            mes1=meses.get(k)
    print(dia,"de",mes1,"de",año)

    
fecha=input("Introduce una fecha en formato dd/mm/aaaa: ")
nombre_mes(fecha)
