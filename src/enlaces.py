import json
import os

def abrir_archivo(ruta):
    if os.path.exists(ruta) == False:
        return False
    archivo = open(ruta, 'r', encoding='utf-8')
    obj_json = json.loads(archivo.read())
    archivo.close()
    return obj_json

def escribir_archivo(ruta, datos):
        #Revisar si el archivo el existe
    if os.path.exists(ruta) == False:
        return False
    
    archivo = open(ruta,'w',encoding='utf-8')
    #Se transforman los datos de un tipo objecto (object) a un tipo String, porque el archivo solo entiende de strings
    string_datos = json.dumps(datos,ensure_ascii=False)
    #Se escribe ese string
    archivo.write(string_datos)
    #Se cierra
    archivo.close()
    return True

if __name__ == '__main__':
    pass