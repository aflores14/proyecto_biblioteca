#crea alta json para socio.json

import json
import os
import time
from src.enlaces import *
from socio import ultimo_codigo,solicitar_fecha_separada
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

def ingresar_valor(mensaje):
    valor = input(mensaje)
    while valor.strip() =="":
         valor = input(mensaje)
    return valor

def registrar_socio(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    id_socio = ultimo_codigo(ruta_socios) + 1
    print("Campos obligatorios")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    fecha_nacimiento = str(solicitar_fecha_separada())
    direccion = input("Ingrese direccion: ")
    correo_electronico = input("Ingrese correo electronico: ")
    telefono = input("Ingrese telefono: ")
    # estado = input("Ingrese estado (1 para activo): ")
    persona = {
        "id_socio": id_socio,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": direccion,
        "correo_electronico": correo_electronico,
        "telefono": telefono,
        "estado": "1"
    }
    personas.append(persona)
    escribir_archivo(ruta_socios,personas)


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

valor = ingresar_valor("Ingrese un valor:")
print(valor)