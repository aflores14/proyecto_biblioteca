#Archivo socios

import json
import os

# abrir json
def abrir_archivo(ruta):
    if os.path.exists(ruta) == False:
        return False
    archivo = open(ruta, 'r', encoding='utf-8')
    obj_json = json.loads(archivo.read())
    archivo.close()
    return obj_json

#registrar campo nuevo en socios.json con los datos

def registrar_persona(ruta, persona):
    personas = abrir_archivo(ruta)
    personas.append(persona)
    archivo = open(ruta, 'w', encoding='utf-8')
    archivo.write(json.dumps(personas))

#registrar campo nuevo en socios.json con los datos

def modificar_persona(ruta, persona):
    personas = abrir_archivo(ruta)
    personas.append(persona)
    archivo = open(ruta, 'w', encoding='utf-8')
    archivo.write(json.dumps(personas))



#listar socios
def listar_personas(ruta):
    personas = abrir_archivo(ruta)
    if len(personas) == 0:
        print('No hay personas en la Base de Datos.')
    for persona in personas:
        print(persona)

#inicio

ruta = './proyecto_biblioteca/src/socios.json'
listar_personas(ruta)