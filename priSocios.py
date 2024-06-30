import os
from src.enlaces import abrir_archivo
from socio import registrar_socio,modificarSocio,mostrar_lista,modificarEstado,devolver_noeliminados
from funcionalidad.abm import buscar_registro


ruta_socios = './src/socios.json'
# ruta_prestamos = './src/prestamos.json'

# Función para limpiar la pantalla
def limpiar_pantalla():
    # Comando para Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para Unix/Linux/Mac
    else:
        os.system('clear')

# Función para mostrar el menú con líneas continuas ASCII
def mostrar_menu():
    print("┌───────────────────────────────┐")
    print("│          MENÚ SOCIOS          │")
    print("├───────────────────────────────┤")
    print("│ 1. Registrar Socio            │")
    print("│ 2. Editar Socio               │")
    print("│ 3. Baja Socios                │")
    print("│ 4. Listar Socios              │")    
    print("│ 0. Volver                     │")
    print("└───────────────────────────────┘")

# Funciones para cada opción del menú
def opcion4():
    lista = abrir_archivo(ruta_socios)
    mostrar_lista(lista)
    input("Presiona Enter para continuar...")
    limpiar_pantalla()

def opcion2():
    try:
        dato = input("Ingrese el apellido del Socio: ")
        listaSocios = buscar_registro(ruta_socios,"apellido",dato)
        limpiar_pantalla()
        activos = devolver_noeliminados(listaSocios) 
        if not activos:
            input("\nNo hay socios con el apellido ingresado. Volviendo..")
            pass
        else:
            mostrar_lista(activos)
            id = int(input("\nIngrese el ID del socio a modificar: "))
            modificarSocio(ruta_socios,id)
            input("Operacion realizada. Presiona Enter para continuar...")
    except ValueError as e:
        # print("Valor inválido:", e)
        input("Error!!. Volviendo al Menu...")
    limpiar_pantalla()

def opcion3():
    try:
        dato = input("\nIngrese el apellido del Socio: ")
        listaSocios = buscar_registro(ruta_socios,"apellido",dato)
        limpiar_pantalla()
        activos = devolver_noeliminados(listaSocios) 
        if not activos:
            input("\nNo hay socios con el apellido ingresado. Volviendo..")
            pass
        else:
            mostrar_lista(activos)
            id = int(input("\nIngrese el ID del socio a modificar: "))
            if modificarEstado(ruta_socios, id ,"0"):
                input("\nSocio Eliminado. Presiona Enter para continuar...")
            else:
                input("\nSocio no encontrado. Presiona Enter para continuar...")
    except ValueError as e:
        # print("Valor inválido:", e)
        input("Error!!. Volviendo al Menu...")
    limpiar_pantalla()

# Función principal que ejecuta el menú
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_socio(ruta_socios)
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            opcion4()            
        elif opcion == "0":
            print("Saliendo del menú. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...")
            limpiar_pantalla()

# Ejecutar el programa
if __name__ == "__main__":
    main()
