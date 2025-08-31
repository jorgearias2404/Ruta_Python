#se le asigna valores por defecto a los argumentos
def find_volume(len = 1,width = 1,depth= 1):
    return len * width * depth,width,'Hola'

#asi podemos asiganar al argumento que queramos
#un valor de forma directa
resul = find_volume(width = 10) 

#alamacen resultado de op, ancho y el texto
result2,width,text = find_volume(width = 10) 