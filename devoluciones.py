
from datetime import datetime
from src.enlaces import *


ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'
ruta_libros = './src/libros.json'


# devolver libro

def buscaridprestamo(ruta_prestamos):
    prestamos = abrir_archivo(ruta_prestamos)
    libros = abrir_archivo(ruta_libros)
    busprestamo = int(input("ingrese numero de id_prestamo: "))
    encontrado = next((x for x in prestamos if x['id_prestamo'] == busprestamo), "no existe prestamo con ese id")
    print(encontrado)
    for prestamo in prestamos:
        if prestamo['id_prestamo'] == busprestamo:
            prestamo['fecha_entrega'] = datetime.now().strftime('%Y-%m-%d')
            for libro in libros:
              if libro['id_libro'] == prestamo['id_libro']:
                    libro['cantidad_disponible'] += 1
                    print("El libro se ha devuelto")
            prestamos.append(prestamo)
            escribir_archivo(ruta_libros,libros)
            escribir_archivo(ruta_prestamos,prestamos)
            break        
        
def main():
    
    buscaridprestamo(ruta_prestamos)
    
if __name__ == '__main__':
    main()
