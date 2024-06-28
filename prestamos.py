#Archivo prestamos
from datetime import datetime
from src.enlaces import *
from funcionalidad.conexion.rutas import obtener_ruta_libro,existe_archivo
import datetime as dt

ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'
ruta_libros = './src/libros.json'


def generaridprestamo(ruta_prestamos):
    prestamos = abrir_archivo(ruta_prestamos)
    if len(prestamos) == 0:
        return 0
    return prestamos[-1]['id_prestamo']

def buscar_registro(ruta,campo,dato):
    lista_busqueda = []
    lista = existe_archivo(ruta)
    if len(lista) == 0:
        print('No hay datos registrados')
        return lista_busqueda
    else:
        for diccionario in lista:
            for clave,valor in diccionario.items():
                if campo==clave and valor.find(dato)>=0:
                    lista_busqueda.append(diccionario['id_libro'])
                    lista_busqueda.append(diccionario['titulo'])
                    lista_busqueda.append(diccionario['autor'])
    return lista_busqueda


def buscarsocio(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    prestamos = abrir_archivo(ruta_prestamos)
    libros = abrir_archivo(ruta_libros)
    socio = int(input("ingrese el numero de socio: "))
    for persona in personas:
        if persona['id_socio'] == socio and persona['estado'] == "1":
            print("nombre de socio: ", persona['nombre'])
            valor = int(input("coloque 1 para buscar por nombre de libro o 2 para buscar por autor: "))
            if valor == 1:
                dato = input("ingrese nombre del libro: ")
                mostrar = buscar_registro(obtener_ruta_libro(),'titulo',dato)
                print(mostrar)
                id_libro = int(input("ingrese el id del libro a prestar: "))
                for libro in libros:
                    print(libro['id_libro'])
                    if libro['id_libro'] == id_libro and libro['cantidad_disponible'] != 0:
                        print("cargar informacion")      
                        id_prestamo = generaridprestamo(ruta_prestamos) + 1
                        id_socio = persona['id_socio']
                        id_libro = libro['id_libro']
                        libro['cantidad_disponible'] = libro['cantidad_disponible'] -1
                        fecha_prestamo = datetime.now().strftime('%Y-%m-%d')
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
                        escribir_archivo(ruta_libros, libros)


def main():
   buscarsocio(ruta_socios)

if __name__ == '__main__':
    main()
