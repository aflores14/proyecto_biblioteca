from conexion.rutas import obtener_ruta_libro,existe_archivo
from json import dumps

#*****************************************************************************
def leer_registros(ruta):
    lista = existe_archivo(ruta)
    if len(lista) == 0:
        print('No hay datos registrados')
        return lista
    else:
        for diccionario in lista:
            frase = ''
            print('----------------------------------')
            for clave,valor in diccionario.items():
                frase += f"Campo: {clave}: {valor} -" 
            print(frase)
        return lista
#*****************************************************************************
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
                    lista_busqueda.append(diccionario)
    return lista_busqueda
#*****************************************************************************
def registros_iguales(actual,nuevo,opc):
    match opc:
        case 0:
            if (actual['titulo'].upper() == nuevo['titulo'].upper() and 
                actual['autor'].upper() == nuevo['autor'].upper() and 
                actual['editorial'].upper() == nuevo['editorial'].upper() and
                actual['año_publicacion'] == nuevo['año_publicacion'] and
                actual['genero'].upper() == nuevo['genero'].upper()):
                return True
        case 1:
                return True
        case 2:
                return True
    return False
def agregar_registro(ruta,nuevo,opc):
    lista = existe_archivo(ruta)
    if len(lista) == 0:
        print('No hay datos registrados')
        return False
    else:
        posicion = 0
        for actual in lista:
            existe = registros_iguales(actual,nuevo,opc)
            if existe:
                break
            else:
                posicion += 1
        if existe:
            lista[posicion]['cantidad_disponible'] += 1
        else:
            match opc:
                case 0:
                    nuevo['id_libro'] = len(lista) + 1
                    nuevo['cantidad_disponible'] = 0
                    nuevo['eliminado'] = 0
            lista.append(nuevo)
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(dumps(lista,ensure_ascii=False))
        archivo.close()
        return True
#*****************************************************************************
def registros_iguales2(actual,id,opc):
    match opc:
        case 0:
            if actual['id_libro'] == id:
                return True
        case 1:
                return True
        case 2:
                return True
    return False
def modificar_registro(ruta,registro,opc):
    lista = existe_archivo(ruta)
    if len(lista) == 0:
        print('No hay datos registrados')
        return False
    else:
        for actual in lista:
            if registros_iguales2(actual,registro['id_libro'],opc):
                match opc:
                    case 0:
                        actual['titulo'] = registro['titulo']
                        actual['autor'] = registro['autor']
                        actual['editorial'] = registro['editorial']
                        actual['año_publicacion'] = registro['año_publicacion']
                        actual['genero'] = registro['genero']
                    case 1:
                        print('socio')
                break
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(dumps(lista,ensure_ascii=False))
        archivo.close()
        return True
#*****************************************************************************
def elimiar_registro(ruta,registro,opc,motivo):
    lista = existe_archivo(ruta)
    if len(lista) == 0:
        print('No hay datos registrados')
        return False
    else:
        for actual in lista:
            if registros_iguales2(actual,registro['id_libro'],opc):
                if actual['cantidad_disponible'] > 0:
                    actual['cantidad_disponible'] -= 1
                    actual['cantidad_eliminados'] += 1
                    actual['motivos_eliminados'].append(motivo)
                    break
                else:
                    print('No se puede eliminar')
                    return False
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(dumps(lista,ensure_ascii=False))
        archivo.close()
        return True
#*****************************************************************************
#leer_json(obtener_ruta_libro())
#l = buscar_diccionario(obtener_ruta_libro(),'titulo','dad')
#print(l)
libro =   {
      "id_libro": 1,
      "titulo": "Cien Años de SoledaD",
      "autor": "Gabriel García Márquez",
      "editorial": "Sudamericana",
      "año_publicacion": 1967,
      "genero": "Novela",
      "cantidad_disponible": 0,
      "eliminados" : 0
  }
#agregar_registro(obtener_ruta_libro(),libro,0)
#modificar_registro(obtener_ruta_libro(),libro,0)

#eliminar_registro(obtener_ruta_libro(),libro,0)