import os
from socio import registrar_socio,modificarSocio,mostrar_lista
from funcionalidad.abm import buscar_registro


ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'

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
    print("│ 4. Volver                     │")
    print("└───────────────────────────────┘")

# Funciones para cada opción del menú
def opcion1():
    print("Has seleccionado la opción 1.")
    input("Presiona Enter para continuar...")
    limpiar_pantalla()

def opcion2():
    print("Has seleccionado la opción 2.")
    input("Presiona Enter para continuar...")
    limpiar_pantalla()

def opcion3():
    print("Has seleccionado la opción 3.")
    input("Presiona Enter para continuar...")
    limpiar_pantalla()

# Función principal que ejecuta el menú
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_socio(ruta_socios)
        elif opcion == "2":
            dato = input("Ingrese el apellido del Socio")
            mostrar_lista(buscar_registro(ruta_socios,"apellido",dato))
            break
            modificarSocio(ruta_socios)
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print("Saliendo del menú. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...")
            limpiar_pantalla()

# Ejecutar el programa
if __name__ == "__main__":
    main()
