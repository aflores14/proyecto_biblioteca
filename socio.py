#Archivo socios
import json
import os
from datetime import datetime
from src.enlaces import *

# baja socio: modifica el estado de un socio, 1 para activo , 0 para incactivo y -1 para suspendido
def modificarEstado(ruta, id_socio,estado):
    personas = abrir_archivo(ruta)
    for persona in personas:
        if persona['id_socio'] == id_socio:
            persona['estado'] = estado



# modificar socio, cambia los campos de una persona segun el id_socio
# def modificarSocio(ruta, id_socio):
#     personas = abrir_archivo(ruta)
#     for persona in personas:
#         if persona['id_socio'] == id_socio:
#             persona['nombre'] = input("Ingresar el nombre: ")
#             persona['apellido'] = input("Ingresar el apellido: ")
#             persona['dni'] = input("Ingresar el dni: ")
#             persona['fecha_nacimiento'] = input("Ingresar la fecha de nacimiento: ")
#             persona['direccion'] = input("Ingresar la direccion: ")
#             persona['telefono'] = input("Ingresar el telefono: ")
#             persona['email'] = input("Ingresar el email: ")
#             persona['estado'] = input("Ingresar el estado: ")
#             persona['fecha_alta'] = input("Ingresar la fecha de alta: ")


#registrar campo nuevo en socios.json con los datos

# def registrar_persona(ruta, persona):
#     personas = abrir_archivo(ruta)
#     personas.append(persona)
#     archivo = open(ruta, 'w', encoding='utf-8')
#     archivo.write(json.dumps(personas))

#fechas
def solicitar_fecha_separada():
    while True:
        try:
            dia = int(input("Ingresa el día (1-31): "))
            mes = int(input("Ingresa el mes (1-12): "))
            año = int(input("Ingresa el año (ejemplo: 2024): "))
            
            # Intentar crear una fecha con los valores ingresados
            fecha_validada = datetime(año, mes, dia)
            print("Fecha válida:", fecha_validada.strftime("%d/%m/%Y"))
            return fecha_validada.strftime("%d/%m/%Y")
        except ValueError as e:
            print("Fecha inválida:", e)
            print("Por favor, intenta de nuevo con valores correctos.")

#registrar campo nuevo en socios.json con los datos
# def modificar_persona(ruta, persona):
#     personas = abrir_archivo(ruta)
#     personas.append(persona)
#     archivo = open(ruta, 'w', encoding='utf-8')
#     archivo.write(json.dumps(personas))


#consultar el ultimo id_socio de socio, devulve el valor
def ultimo_codigo(ruta):
    personas = abrir_archivo(ruta)
    if len(personas) == 0:
        return 0
    return personas[-1]['id_socio']

#listar socios
def listar_personas(ruta):
    personas = abrir_archivo(ruta)
    if len(personas) == 0:
        print('No hay personas en la Base de Datos.')
    for persona in personas:
        print(persona)

#registrar nuevo socio

def registrar_socio(ruta):
    personas = abrir_archivo(ruta)
    id_socio = ultimo_codigo(ruta) + 1
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
    escribir_archivo(ruta,personas)

def main():
    #inicio
    ruta = './proyecto_biblioteca/src/socios.json'
    registrar_socio(ruta)
    listar_personas(ruta)


if __name__ == '__main__':
    main()