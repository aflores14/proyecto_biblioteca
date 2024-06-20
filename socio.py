#Archivo socios

import json
import os
from datetime import datetime

# abrir json
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
    
    archivo = open(ruta, 'w')
    #Se transforman los datos de un tipo objecto (object) a un tipo String, porque el archivo solo entiende de strings
    string_datos = json.dumps(datos)
    #Se escribe ese string
    archivo.write(string_datos)
    #Se cierra
    archivo.close()
    return True


#registrar campo nuevo en socios.json con los datos

def registrar_persona(ruta, persona):
    personas = abrir_archivo(ruta)
    personas.append(persona)
    archivo = open(ruta, 'w', encoding='utf-8')
    archivo.write(json.dumps(personas))

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
            return fecha_validada
        except ValueError as e:
            print("Fecha inválida:", e)
            print("Por favor, intenta de nuevo con valores correctos.")
#registrar campo nuevo en socios.json con los datos

def modificar_persona(ruta, persona):
    personas = abrir_archivo(ruta)
    personas.append(persona)
    archivo = open(ruta, 'w', encoding='utf-8')
    archivo.write(json.dumps(personas))


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

#registrar nuevo socio con datos  "nombre": "Carlos",
        # "apellido":
        # "fecha_nacimiento": 
        # "direccion": 
        # "correo_electronico": 
        # "telefono": 
        # "estado": 

def registrar_socio(ruta):
    personas = abrir_archivo(ruta)
    id_socio = str(int(ultimo_codigo(ruta)) + 1)
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
    # print(persona)
    personas.append(persona)
    escribir_archivo(ruta,personas)




#inicio

ruta = './proyecto_biblioteca/src/socios.json'
registrar_socio(ruta)
listar_personas(ruta)
# print(ultimo_codigo(ruta))
# print("ultimo codigo de socios: " , ultimo_codigo(ruta))