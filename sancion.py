#Archivo socios
from datetime import datetime, timedelta
from socio import ultimo_codigo
from src.enlaces import *

ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'
ruta_sanciones = './src/sanciones.json'

# Si la fecha de devolucion supero a la fecha actual, el libro no fue devuelto
#  y no tiene ya sancion por ese prestamos se sanciona
def actualizarEstadoSocios(ruta_socios,ruta_prestamos):
    prestamos = abrir_archivo(ruta_prestamos)
    socios = abrir_archivo(ruta_socios)
    for prestamo in prestamos:
        # devolucion = datetime.strptime(prestamo['fecha_prestamo'], '%Y-%m-%d') + timedelta(days=7)
        # if prestamo['estado_prestamo'] == "En Curso" and devolucion.strftime('%Y-%m-%d') < datetime.now().strftime('%Y-%m-%d') :
        if prestamo['fecha_entrega'] == "" and (prestamo['fecha_devolucion'] < datetime.now().strftime('%Y-%m-%d')):
            # sancionar
            # controlamos que no se realizo ya la sancion por ese prestamo
            sanciones = abrir_archivo(ruta_sanciones)
            valor_no_presente = True
            for sancion in sanciones:
                if sancion['id_prestamo'] == prestamo['id_prestamo']:
                    valor_no_presente = False
            if valor_no_presente:
                #crear sancion
                id_sancion = ultimo_codigo(ruta_sanciones,"id_sancion") + 1
                dias_sancion = datetime.strptime(prestamo['fecha_prestamo'],'%Y-%m-%d') + timedelta(days=7)
                sancion = {
                    'id_sancion': id_sancion,
                    'id_socio': prestamo['id_socio'],
                    'id_prestamo': prestamo['id_prestamo'],
                    'fecha_inicio': datetime.now().strftime('%Y-%m-%d'),
                    'fecha_fin': dias_sancion.strftime('%Y-%m-%d'),
                    'motivo': "libro no devuelto",
                    'estado': "activa",
                }
                #cambiar estado socio a -1
                for socio in socios:
                    if socio['id_socio'] == prestamo['id_socio']:
                        socio['estado'] = "-1"
                escribir_archivo(ruta_socios,socios)
                #agregar sancion
                sanciones.append(sancion)
                escribir_archivo(ruta_sanciones, sanciones)

#  verifico si los que tiene estado "-1", busco en sanciones la de estado activa para ese id
# en prestamos verifico la devolucion y la fecha de fin de la sancion
# cambio el estado de la sancion a "cumplido" y en el socio cambio su "estado" a "1"
def quitarSanciones(ruta_socios,ruta_prestamos,ruta_sanciones):
    socios = abrir_archivo(ruta_socios)
    prestamos = abrir_archivo(ruta_prestamos)
    sanciones = abrir_archivo(ruta_sanciones)
    for socio in socios:
        if socio['estado'] == "-1":
            for sancion in sanciones:
                if sancion['id_socio'] == socio['id_socio'] and sancion['estado'] == "activa":
                    for prestamo in prestamos:
                        if prestamo['id_prestamo'] == sancion['id_prestamo']:
                            if prestamo['fecha_entrega']!= "" and sancion['fecha_fin'] < datetime.now().strftime('%Y-%m-%d'):
                                sancion['estado'] = "cumplido"
                                socio['estado'] = "1"
                                #guardo
                                escribir_archivo(ruta_sanciones, sanciones)
                                escribir_archivo(ruta_socios, socios)



def main():
    quitarSanciones(ruta_socios,ruta_prestamos,ruta_sanciones)
    actualizarEstadoSocios(ruta_socios,ruta_prestamos)
if __name__ == '__main__':
    main()