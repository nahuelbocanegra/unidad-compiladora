from crud_dispositivos import *
from dispositivos import controlar_aire

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
            eliminar_dispositivos()
        elif opcion == 5:
            controlar_aire()
        elif opcion == 6:
            print("vuelva pronto! ")
            break
        else:
            print("por favor ingrese un numero del 1 al 5")

    except:
        print("Entrada no valida,por favor ingrese un numero del 1 al 5")