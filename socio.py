#Archivo socios
from datetime import datetime
from src.enlaces import *

ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'

# suspender socio
def suspenderSocios(ruta_socios,ruta_prestamos):
    personas = abrir_archivo(ruta_socios)
    prestamos = abrir_archivo(ruta_prestamos)
    for prestamo in prestamos:
        if prestamo['estado_prestamo'] == "En Curso":
            prestamo['estado'] = -1

#mostrar lista en un recuadro usando ascci
def mostrar_lista(lista,campo1,campo2,campo3):
    print("\t┌───────────────────────────────┐")
    print("\t│            LISTAR             │")
    print("\t└───────────────────────────────┘")
    for persona in lista:
        if campo3:
            print(f"\t  ID:{persona[campo1]}\t{persona[campo2]}, {persona[campo3]}")
    print("\t─────────────────────────────────")
# devolver una lista con solo los socios que no tengan estado 0
def devolver_noeliminados(personas):
    return [persona for persona in personas if persona['estado']!= "0"]

# baja socio: modifica el estado de un socio, 1 para activo , 0 para inactivo y -1 para suspendido
def modificarEstado(ruta_socios, id_socio,estado):
    personas = abrir_archivo(ruta_socios)
    bandera = False
    for persona in personas:
        if persona['id_socio'] == id_socio:
            persona['estado'] = estado
            escribir_archivo(ruta_socios,personas)
            print(f"Socio: {persona['apellido']} {persona['nombre']} ACTUALIZADO")
            bandera = True
    return bandera

# Modificar socio, por numero id
def modificarSocio(ruta_socios, id_socio):
    personas = abrir_archivo(ruta_socios)
    bandera = True
    for persona in personas:
        if persona['id_socio'] == id_socio:
            bandera = False
            print("\nModificar Persona. Para no modificarla, dejar el espacio en blanco presionando ‘Enter’")
            persona['nombre'] = input(f"Nombre ({persona['nombre']}): ") or persona['nombre']
            persona['apellido'] = input(f"Apellido ({persona['apellido']}): ") or persona['apellido']
            opcion1 = input(f"¿Modificar la fecha de nacimiento ({persona['fecha_nacimiento']}?). Si o dejar el espacio en blanco presionando ‘Enter’ para no modificar: ")
            if opcion1 != '':            
                persona['fecha_nacimiento'] = str(solicitar_fecha_separada())
            persona['direccion'] = input(f"Direccion ({persona['direccion']}): ") or persona['direccion']
            persona['telefono'] = input(f"Telefono ({persona['telefono']}): ") or persona['telefono']
            persona['correo_electronico'] = input(f"Correo electronico ({persona['correo_electronico']}): ") or persona['correo_electronico']
            # print(persona)
    if bandera:
        print(f"\nNo se encontró el socio con ID {id_socio}")
        return None
    escribir_archivo(ruta_socios,personas)

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


#consultar el ultimo id_socio de socio, devulve el valor
def ultimo_codigo(ruta_socios,id = 'id_socio'):
    personas = abrir_archivo(ruta_socios)
    if len(personas) == 0:
        return 0
    return personas[-1][id]

#listar socios
def listar_personas(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    if len(personas) == 0:
        print('No hay personas en la Base de Datos.')
    for persona in personas:
        print(persona)

def ingresar_valor(mensaje):
    valor = input(mensaje)
    while valor.strip() =="":
         valor = input(mensaje)
    return valor

#registrar nuevo socio
def registrar_socio(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    id_socio = ultimo_codigo(ruta_socios,"id_socio") + 1
    print("Campos obligatorios")
    nombre = ingresar_valor("Ingrese nombre: ")
    apellido = ingresar_valor("Ingrese apellido: ")
    print("Ingrese fecha de nacimiento")
    fecha_nacimiento = str(solicitar_fecha_separada())
    direccion = ingresar_valor("Ingrese direccion: ")
    correo_electronico = ingresar_valor("Ingrese correo electronico: ")
    telefono = ingresar_valor("Ingrese telefono: ")
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
    # listar_personas(ruta_socios)
    modificarSocio(ruta_socios,7)
    # registrar_socio(ruta_socios)
    # listar_personas(ruta_socios)

if __name__ == '__main__':
    main()