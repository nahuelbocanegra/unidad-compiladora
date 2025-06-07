from dispositivos import dispositivos
from crud_dispositivos import (
    listar_dispositivos,
    buscar_dispositivos,
    agregar_dispositivos,
    eliminar_dispositivos,
    cambiar_estado,
    modificar_dispositivo,
    consultar_estado
)


def dispo():
    
    while True:

        print("\n1 - Listar dispositivo ")
        print("2 - Buscar dispositivo ")
        print("3 - Agregar dispositivo ")
        print("4 - Eliminar dispositivo ")
        print("5 - Controlar aire")
        print("6 - Salir \n")



        try:
            opcion = int(input("Elija una opcion:   "))
            

            if opcion == 1:
                listar_dispositivos()
            elif opcion == 2:
                nombre_dispositivo=input("Ingrese el nombre de dispositivo que desea buscar: ")
                print(buscar_dispositivos(nombre_dispositivo))
            elif opcion == 3:
                nuevo_dispositivo=input("Ingrese el nombre de dispositivo que desea agregar: ")
                agregar_dispositivos(nuevo_dispositivo)
            elif opcion == 4:
                dispositivo=input("Ingrese el nombre de dispositivo que desea eliminar: ")
                eliminar_dispositivos(dispositivo)
            elif opcion == 5:
                controlar_aire()
            elif opcion == 6:
                print("vuelva pronto! ")
                break
            else:
                print("por favor ingrese un numero del 1 al 5")

        except:
            print("Entrada no valida,por favor ingrese un numero del 1 al 5")

def mostrar_menu():
    while True:
        print("\n=== Menú de Dispositivos Inteligentes ===")
        print("1. Listar dispositivos")
        print("2. Buscar dispositivo")
        print("3. Agregar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Cambiar estado de dispositivo")
        print("6. Modificar dispositivo")
        print("7. Consultar estado del dispositivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_dispositivos()

        elif opcion == "2":
            nombre = input(" Ingrese el nombre del dispositivo a buscar: ")
            print(buscar_dispositivos(nombre))

        elif opcion == "3":
            nombre = input(" Ingrese el nombre del nuevo dispositivo: ")
            print(agregar_dispositivos(nombre))

        elif opcion == "4":
            nombre = input(" Ingrese el nombre del dispositivo a eliminar: ")
            eliminar_dispositivos(nombre)

        elif opcion == "5":
            nombre = input("Ingrese el nombre del dispositivo: ")
            estado = input("¿Encender? (s/n): ").lower() == "s"
            cambiar_estado(nombre, estado)

        elif opcion == "6":
            nombre = input(" Ingrese el nombre del dispositivo: ")
            clave = input(" Ingrese el atributo a modificar (ej: 'ubicacion', 'tipo'): ")
            valor = input(" Ingrese el nuevo valor: ")
            modificar_dispositivo(nombre, **{clave: valor})

        elif opcion == "7":
            nombre = input(" Ingrese el nombre del dispositivo: ")
            consultar_estado(nombre)

        elif opcion == "8":
            print("fin de sesion!")
            break

        else:
            print(" Opción inválida. Por favor intente de nuevo.")

