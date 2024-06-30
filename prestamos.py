#Archivo prestamos
import datetime
from datetime import datetime
from datetime import timedelta
from src.enlaces import *
from funcionalidad.conexion.rutas import obtener_ruta_libro,existe_archivo
import pprint

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
                if isinstance(dato, int):
                    if campo==clave and valor==dato:
                        print("clave.-",clave)
                        print("dato.-",dato)
                       # pasusa = input("Eserar..int")
                        nuevo_diccionario = {clave: valor for clave, valor in diccionario.items() if clave in ['id_libro', 'titulo', 'autor']}
                        lista_busqueda.append(diccionario)
                elif isinstance(dato, str):
                    if campo==clave and valor.lower().find(dato.lower())>=0:
                        #pasusa = input("Eserar..str")
                        nuevo_diccionario = {clave: valor for clave, valor in diccionario.items() if clave in ['id_libro', 'titulo', 'autor']}
                        lista_busqueda.append(nuevo_diccionario)
    return lista_busqueda

def menu():
    print("Buscar libro por autor o titulo")
    print("1. Buscar por autor")
    print("2. Buscar por nombre de libro")
    print("3. Continuar")
    opcion = int(input("Elija una opcion: "))
    return opcion


def buscarsocio(ruta_socios):
    personas = abrir_archivo(ruta_socios)
    prestamos = abrir_archivo(ruta_prestamos)
    libros = abrir_archivo(ruta_libros)
    socio = int(input("ingrese el numero de socio: "))
    for persona in personas:
         if persona['id_socio'] == socio and persona['estado'] == 1:
             encontrado = 1
             socio_prestamo = persona ['id_socio']
             print("SOCIO ENCONTRADO")
             print("Nombre: ",persona['nombre'])
             print("Apellido: ",persona['apellido'])
             print("Fecha de nacimiento: ", persona['fecha_nacimiento'])
             break
         elif persona['id_socio'] == socio and persona ['estado'] == -1:
             encontrado = -1
             print("SOCIO ENCONTRADO - SUSPENDIDO NO PUEDE SOLICITAR PRESTAMO")
             print("Nombre: ",persona['nombre'])
             print("Apellido: ",persona['apellido'])
             print("Fecha de nacimiento: ", persona['fecha_nacimiento'])
             break
         elif persona['id_socio'] == socio and persona ['estado'] == 0:
             encontrado = 0
             print("SOCIO ENCONTRADO - CUENTA ELIMINADA POR REINCIDENCIA")
             print("Nombre: ",persona['nombre'])
             print("Apellido: ",persona['apellido'])
             print("Fecha de nacimiento: ", persona['fecha_nacimiento'])
             break
         else:
             encontrado = 2

    if encontrado == 1:
        print ("socio encontrado")
        print("\t─────────────────────────────────")
        opcion = menu()
        while opcion!= 3:
            if opcion == 1:
                dato = input("ingrese el nombre del autor: ")
                print("\t─────────────────────────────────")
                lista = buscar_registro(ruta_libros,'autor',dato)
                pprint.pprint(lista)
                print("\t─────────────────────────────────")
                encontro = input("¿Encontro el libro?: Si o No: ")
                if encontro.lower() == "si":
                    libro_encontrado = int(input("ingrese el id_libro que va a prestar: "))
                    print("\t─────────────────────────────────")
                    break
                elif encontro.lower() == "no":
                    print("Debe buscar el libro por titulo para encontrarlo")
                
            elif opcion == 2:
                dato = input("ingrese el titulo del libro: ")
                print("\t─────────────────────────────────")
                lista = buscar_registro(ruta_libros,'titulo',dato)
                pprint.pprint(lista)
                print("\t─────────────────────────────────")
                encontro = input("¿Encontro el libro?: Si o No: ")
                if encontro.lower() == "si":
                    libro_encontrado = int(input("ingrese el id_libro que va a prestar: "))
                    print("\t─────────────────────────────────")
                    break
                elif encontro.lower() == "no":
                    print("Debe buscar el libro por autor para encontrarlo")
                print("\t─────────────────────────────────")
            else:
                print("Opcion invalida. Intente nuevamente.")
            opcion = menu()
    elif encontrado == 0:
        print("\t─────────────────────────────────")
        print("NO SE PUEDE PRESTAR - CUENTA ELIMINADA POR REINCIDENCIA")
    elif encontrado == -1:
        print("\t─────────────────────────────────")
        print("NO SE PUEDE PRESTAR - CUENTA SUSPENDIDA POR NO DEVOLVER LIBRO")
    elif encontrado == 2:
        print("\t─────────────────────────────────")
        print("SOCIO NO ENCONTRADO")
    
    for libro in libros:
        if libro['id_libro'] == libro_encontrado and libro['cantidad_disponible'] != 0:
            print("cargar informacion")      
            id_prestamo = generaridprestamo(ruta_prestamos) + 1
            id_socio = socio_prestamo
            id_libro = libro['id_libro']
            libro['cantidad_disponible'] = libro['cantidad_disponible'] -1
            fecha_prestamo = datetime.now().strftime('%Y-%m-%d')
            fecha_devolucion = datetime.strptime(fecha_prestamo, '%Y-%m-%d') + timedelta(days=15)
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
            print("\t─────────────────────────────────")
            print("PRESTAMO REALIZADO EXITOSAMENTE")


def main():
   buscarsocio(ruta_socios)

if __name__ == '__main__':
    main()
