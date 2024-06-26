#Archivo socios
import json
import os
from datetime import datetime, timedelta
from socio import ultimo_codigo
from src.enlaces import *

ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'
ruta_sanciones = './src/sanciones.json'


# suspender socio

def actualizarEstadoSocios(ruta_socios,ruta_prestamos):
    prestamos = abrir_archivo(ruta_prestamos)
    for prestamo in prestamos:
        # devolucion = datetime.strptime(prestamo['fecha_prestamo'], '%Y-%m-%d') + timedelta(days=7)
        # if prestamo['estado_prestamo'] == "En Curso" and devolucion.strftime('%Y-%m-%d') < datetime.now().strftime('%Y-%m-%d') :
        if prestamo['fecha_entrega'] == "" and (prestamo['fecha_devolucion'] < datetime.now().strftime('%Y-%m-%d')):
            # sancionar
            valor_no_presente = True
            sanciones = abrir_archivo(ruta_sanciones)
            for sancion in sanciones:
                if sancion['id_prestamo'] == prestamo['id_prestamo']:
                    valor_no_presente = False
            if valor_no_presente:
                #crear sancion
                id_sancion = ultimo_codigo(ruta_sanciones,"id_sancion") + 1
                print("sanciones",id_sancion)
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
                print(sanciones)
                print(sancion)
                pausas=input('holas') 
                sanciones.append(sancion)
                escribir_archivo(ruta_sanciones, sanciones)

            # print (f"Sancionar a {prestamo['id_socio']}, fecha devolucion:{prestamo['fecha_devolucion']} - hoy: {datetime.now().strftime('%Y-%m-%d')}")
    # print (f"Sancionar, fecha devolucion:{prestamo['fecha_prestamo']} - hoy: {datetime.now().strftime('%Y-%m-%d')}")


def main():
    actualizarEstadoSocios(ruta_socios,ruta_prestamos)

if __name__ == '__main__':
    main()