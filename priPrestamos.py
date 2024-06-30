import os
from src.enlaces import abrir_archivo
from socio import registrar_socio,mostrar_lista,modificarEstado,devolver_noeliminados
from funcionalidad.abm import buscar_registro
from priSocios import limpiar_pantalla

ruta_socios = './src/socios.json'
ruta_prestamos = './src/prestamos.json'

# Función para mostrar el menú con líneas continuas ASCII
def mostrar_menu():
    print("┌─────────────────────────────────┐")
    print("│          MENÚ PRESTAMOS         │")
    print("├─────────────────────────────────┤")
    print("│ 1. Prestamo Libro               │")
    print("│ 2. Devolver Libro               │")
    print("│ 3. Listar Prestamos             │")    
    print("│ 0. Volver                       │")
    print("└─────────────────────────────────┘")

# Funciones para cada opción del menú
def opcion4():
    input("Presio8na Enter para continuar...")
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
            mostrar_lista(activos,"id_socio","nombre","apellido")
            id_prestamos = int(input("\nIngrese el ID del socio para verificar sus prestasmos pendientes: "))
            listaPrestamos = buscar_registro(ruta_prestamos,"id_socio",id_prestamos)
            print(listaPrestamos)
            pasusa = input("Eserar..")
            mostrar_lista(listaPrestamos,"id_prestamo","fecha_devolucion","fecha_entrega")
            # modificarSocio(ruta_socios,id)
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
