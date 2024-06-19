#crea alta json para socio.json
# gosla



import json
import os
import time

def alta_socio():
    #abre el archivo
    archivo = open("socio.json", "r")
    #lee el archivo
    datos = json.load(archivo)
    #cierra el archivo
    archivo.close()
    #abre el archivo
    archivo = open("socio.json", "w")
    #lee el archivo
    datos = json.load(archivo)
    #cierra el archivo
    archivo.close()
