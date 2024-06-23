import os.path as path
from json import dumps,loads

def existe_archivo(file):
    if not path.exists(file):
        f = open(file,"x")
        f.close()
        lista = []
        archivo = open(file, 'w', encoding='utf-8')
        archivo.write(dumps(lista))
        archivo.close()
        return lista
    archivo = open(file, 'r', encoding='utf-8')
    obj_json = loads(archivo.read())
    archivo.close()
    return obj_json

def obtener_ruta_libro():
    return './src/libros.json'

def obtener_ruta_socio():
    return './src/socio.json'

def obtener_ruta_prestamo():
    return './src/prestamo.json'