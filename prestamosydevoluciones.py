#Archivo Registro de Préstamos y Devoluciones:
import json
import os
from datetime import datetime
from src.enlaces import *

ruta_socios = './proyecto_biblioteca/src/socios.json'
ruta_prestamos = './proyecto_biblioteca/src/prestamos.json'
ruta_libros = '.proyectos_biblioteca/src/libros.json'


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

def generaridprestamo(ruta_prestamos):
    prestamos = abrir_archivo(ruta_prestamos)
    if len(prestamos) == 0:
        return 0
    return prestamos[-1]['id_prestamo']


def buscarsocio(ruta_socios, id_socio):
    personas = abrir_archivo(ruta_socios)
    prestamos = abrir_archivo(ruta_prestamos)
    libros = abrir_archivo(ruta_libros)
    socio = input ("ingrese el numero de socio: ")
    nombre_libro = input ("ingrese el nombre del libro: ")
    autor_libro = input ("ingrese el nombre del autor: ")
    for persona in personas:
        if persona['id_socio'] == socio and persona['estado'] == 1:
            for libro in libros:
                if libro['titulo'] == nombre_libro or libro['autor'] == autor_libro:
                    if libro['cantidad_disponible'] != 0:
                        print("CARGA DE INFORMACION") 
                        id_prestamo = generaridprestamo(ruta_prestamos) + 1
                        id_socio = persona['id_socio']
                        id_libro = libro['id_libro']
                        id_cantidaddisponible ['']
                        fecha_prestamo = datetime.date.today()
                        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=15)
                        fecha_entrega = ""
                        prestamo = {
                            "id_prestamo" : id_prestamo,
                            "id_socio" : id_socio,
                            "id_libro" : id_libro,
                            "fecha_prestamo" : fecha_prestamo,
                            "fecha_devolucion" : fecha_devolucion,
                            "fecha_entrega" : fecha_entrega,
                                        }
                        prestamos.append(prestamo)
                        escribir_archivo(ruta_prestamos,prestamos)
                    else:
                        print("No hay disponibilidad para el libro buscado")
                else:
                    print("El libro no se encuentra")
        elif persona['id_socio'] == socio and persona['estado'] == 0:
            print("El socio no se encuentra")
        elif persona['id_socio'] == socio and persona['estado'] == -1:
            print("El socio se encuentra inactivo")

# buscar id de prestamo

def buscaridprestamo(ruta_prestamos, id_prestamo):
    prestamos = abrir_archivo(ruta_prestamos)
    libros = abrir_archivo(ruta_libros)
    busprestamo = int(input("ingrese numero de id_prestamo: "))
    for prestamo in prestamos:
        if prestamo['id_prestamo'] == busprestamo:
            prestamo['fecha_entrega'] = datetime.date.today()
            incrementar_libro = prestamo['id_libro] 
            for libro in libros:
                if libro ['id_libro'] == incrementar_libro:
                    
            
        else:
            print("id_de prestamo no existe vuelva a ingresar")
    escribir_archivo(ruta_prestamos,prestamos)

def main():
    # listar_personas(ruta_socios)
   # buscarsocio(ruta_socios,7)
    buscaridprestamo(ruta_prestamos,1)
    # registrar_socio(ruta_socios)
   # listar_personas(ruta_socios)

if __name__ == '__main__':
    main()
