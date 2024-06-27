mi_lista = [{'id': 1, 'name': 'juan', 'age': 19}, {'id': 2, 'name': 'jose', 'age': 20}, {'id': 3, 'name': 'ana', 'age': 21}]

def buscar_diccionario(lista, clave, valor):
    for diccionario in lista:
        if diccionario[clave] == valor:
            return diccionario
    return None

resultado = buscar_diccionario(mi_lista, 'id', 1)
print(resultado)  # Imprime: {'id': 4, 'name': 'juan', 'age': 19}