#Archivo socios
import json
import os
from datetime import datetime
from src.enlaces import *

ruta_socios = './proyecto_biblioteca/src/socios.json'

# baja socio: modifica el estado de un socio, 1 para activo , 0 para incactivo y -1 para suspendido
def modificarEstado(ruta_socios, id_socio,estado):
    personas = abrir_archivo(ruta_socios)
    for persona in personas:
        if persona['id_socio'] == id_socio:
            persona['estado'] = estado


# Modificar socio, por numero id
def modificarSocio(ruta_socios, id_socio):
    personas = abrir_archivo(ruta_socios)
    for persona in personas:
        if persona['id_socio'] == id_socio:
            print("Modificar Persona. Para no modificarla, dejar el espacio en blanco presionando ‘Enter’")
            persona['nombre'] = input(f"Nombre ({persona['nombre']}): ") or persona['nombre']
            persona['apellido'] = input(f"Apellido ({persona['apellido']}): ") or persona['apellido']
            opcion1 = input(f"Modificar la fecha de nacimiento ({persona['fecha_nacimiento']}). Si o dejar el espacio en blanco presionando ‘Enter’ para no modificar: ")
            if opcion1 != '':            
                persona['fecha_nacimiento'] = str(solicitar_fecha_separada())
            persona['direccion'] = input(f"Direccion ({persona['direccion']}): ") or persona['direccion']
            persona['telefono'] = input(f"Telefono ({persona['telefono']}): ") or persona['telefono']
            persona['correo_electronico'] = input(f"Correo electronico ({persona['correo_electronico']}): ") or persona['correo_electronico']
            print(persona)
    escribir_archivo(ruta_socios,personas)



#registrar campo nuevo en socios.json con los datos

# def registrar_persona(ruta_socios, persona):
#     personas = abrir_archivo(ruta_socios)
#     personas.append(persona)
#     archivo = open(ruta_socios, 'w', encoding='utf-8')
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
# def modificar_persona(ruta_socios, persona):
#     personas = abrir_archivo(ruta_socios)
#     personas.append(persona)
#     archivo = open(ruta_socios, 'w', encoding='utf-8')
#     archivo.write(json.dumps(personas))


#consultar el ultimo id_socio de socio, devulve el valor
def ultimo_codigo(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    if len(personas) == 0:
        return 0
    return personas[-1]['id_socio']

#listar socios
def listar_personas(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    if len(personas) == 0:
        print('No hay personas en la Base de Datos.')
    for persona in personas:
        print(persona)

#registrar nuevo socio

def registrar_socio(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    id_socio = ultimo_codigo(ruta_socios) + 1
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

def main():
    listar_personas(ruta_socios)
    modificarSocio(ruta_socios,4)
    listar_personas(ruta_socios)


if __name__ == '__main__':
    main()