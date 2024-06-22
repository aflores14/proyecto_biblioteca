#crea alta json para socio.json

import json
import os
import time
from src.enlaces import *

ruta_socios = './proyecto_biblioteca/src/socios.json'

# modificar socio, cambia los campos de una persona segun el id_socio, muestras los valores, 
# si no hay cambios deja los valores, sino los actualiza
# modificar socio, cambia los campos de una persona segun el id_socio

def modificarSocio(ruta_socios, id_socio):
    personas = abrir_archivo(ruta_socios)
    for persona in personas:
        if persona['id_socio'] == id_socio:
            print("Modificar Persona. Para no modificarla, dejaré el espacio en blanco presionando ‘Enter’")
            persona['nombre'] = input(f"Nombre ({persona['nombre']}): ") or persona['nombre']
            persona['apellido'] = input(f"Apellido ({persona['apellido']}): ") or persona['apellido']
            persona['fecha_nacimiento'] = input(f"Fecha de nacimiento ({persona['fecha_nacimiento']}): ") or persona['fecha_nacimiento']
            persona['direccion'] = input(f"Direccion ({persona['direccion']}): ") or persona['direccion']
            persona['telefono'] = input(f"Telefono ({persona['telefono']}): ") or persona['telefono']
            persona['correo_electronico'] = input(f"Correo electronico ({persona['correo_electronico']}): ") or persona['correo_electronico']
            print(personas)


'''
def alta_socio():
    #abre el archivo 
    archivo = open("socio.json", "r")
    #lee el archivo
    datos = json.load(archivo)
    #cierra el archivo
    archivo.close()
    #abre el archivo
    archivo = open("socio.json", "w")
    #lee el archivo
    datos = json.load(archivo)
    #cierra el archivo
    archivo.close()
'''

modificarSocio(ruta_socios,4)