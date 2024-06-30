#crea alta json para socio.json

# import json
# import os
# import time
# from datetime import datetime, timedelta
# from src.enlaces import *
# from socio import ultimo_codigo,solicitar_fecha_separada
# ruta_socios = './proyecto_biblioteca/src/socios.json'
# ruta_prestamos = './proyecto_biblioteca/src/prestamos.json'

# modificar socio, cambia los campos de una persona segun el id_socio, muestras los valores, 
# si no hay cambios deja los valores, sino los actualiza
# modificar socio, cambia los campos de una persona segun el id_socio

# def modificarSocio(ruta_socios, id_socio):
#     personas = abrir_archivo(ruta_socios)
#     for persona in personas:
#         if persona['id_socio'] == id_socio:
#             print("Modificar Persona. Para no modificarla, dejaré el espacio en blanco presionando ‘Enter’")
#             persona['nombre'] = input(f"Nombre ({persona['nombre']}): ") or persona['nombre']
#             persona['apellido'] = input(f"Apellido ({persona['apellido']}): ") or persona['apellido']
#             persona['fecha_nacimiento'] = input(f"Fecha de nacimiento ({persona['fecha_nacimiento']}): ") or persona['fecha_nacimiento']
#             persona['direccion'] = input(f"Direccion ({persona['direccion']}): ") or persona['direccion']
#             persona['telefono'] = input(f"Telefono ({persona['telefono']}): ") or persona['telefono']
#             persona['correo_electronico'] = input(f"Correo electronico ({persona['correo_electronico']}): ") or persona['correo_electronico']
#             print(personas)

# def ingresar_valor(mensaje):
#     valor = input(mensaje)
#     while valor.strip() =="":
#          valor = input(mensaje)
#     return valor

# def registrar_socio(ruta_socios):
#     personas = abrir_archivo(ruta_socios)
#     id_socio = ultimo_codigo(ruta_socios) + 1
#     print("Campos obligatorios")
#     nombre = input("Ingrese nombre: ")
#     apellido = input("Ingrese apellido: ")
#     fecha_nacimiento = str(solicitar_fecha_separada())
#     direccion = input("Ingrese direccion: ")
#     correo_electronico = input("Ingrese correo electronico: ")
#     telefono = input("Ingrese telefono: ")
#     # estado = input("Ingrese estado (1 para activo): ")
#     persona = {
#         "id_socio": id_socio,
#         "nombre": nombre,
#         "apellido": apellido,
#         "fecha_nacimiento": fecha_nacimiento,
#         "direccion": direccion,
#         "correo_electronico": correo_electronico,
#         "telefono": telefono,
#         "estado": "1"
#     }
#     personas.append(persona)
#     escribir_archivo(ruta_socios,personas)


# def suspenderSocios(ruta_socios,ruta_prestamos):
#     personas = abrir_archivo(ruta_socios)
#     prestamos = abrir_archivo(ruta_prestamos)
    
#     for prestamo in prestamos:
#         devolucion = datetime.strptime(prestamo['fecha_prestamo'], '%Y-%m-%d') + timedelta(days=7)
#         # OP 2 if prestamo['estado_prestamo'] == "En Curso" and prestamo['fecha_prestamo'] < datetime.now().strftime('%Y-%m-%d') :
#         if prestamo['estado_prestamo'] == "En Curso" and devolucion.strftime('%Y-%m-%d') < datetime.now().strftime('%Y-%m-%d') :
#             print (f"Sancionar a {prestamo['id_socio']}, fecha devolucion:{devolucion.strftime('%Y-%m-%d')} - hoy: {datetime.now().strftime('%Y-%m-%d')}")
#     # print (f"Sancionar, fecha devolucion:{prestamo['fecha_prestamo']} - hoy: {datetime.now().strftime('%Y-%m-%d')}")



# #print(datetime.now().strftime('%Y-%m-%d'))
# suspenderSocios(ruta_socios,ruta_prestamos)
# # from datetime import datetime

# # # Definir las fechas en formato de cadena de texto
# # fecha_str1 = '2024-06-23'  # por ejemplo, la fecha de hoy
# # fecha_str2 = '2024-07-23'  # una fecha futura para el ejemplo

# # # Convertir las cadenas de texto a objetos datetime
# # fecha_dt1 = datetime.strptime(fecha_str1, '%Y-%m-%d')
# # fecha_dt2 = datetime.strptime(fecha_str2, '%Y-%m-%d')

# # # Calcular la diferencia entre las dos fechas
# # diferencia = fecha_dt2 - fecha_dt1

# # print(f'La diferencia entre las fechas es de {diferencia.days} días.')


# # import sys
# # from PySide6.QtWidgets import QApplication, QPushButton

# # # Esta función se llamará cuando se presione el botón
# # def saludar():
# #     print("¡Hola desde el botón!")

# # # Crear la aplicación Qt
# # app = QApplication(sys.argv)

# # # Crear el botón y configurar su texto
# # boton = QPushButton("Haz clic aquí")
# # boton.clicked.connect(saludar)  # Conectar la señal clicked al slot saludar

# # # Mostrar el botón
# # boton.show()

# # # Ejecutar el bucle principal de la aplicación
# # sys.exit(app.exec_())

import sys
import time

def barra_de_progreso(progreso, total):
    porcentaje = 100 * (progreso / total)
    barra = '█' * int(porcentaje) + '-' * (100 - int(porcentaje))
    sys.stdout.write(f'\r[{barra}] {porcentaje:.2f}%')
    sys.stdout.flush()

# Ejemplo de uso
for i in range(101):
    time.sleep(0.05)  # Simula una tarea
    barra_de_progreso(i, 100)
