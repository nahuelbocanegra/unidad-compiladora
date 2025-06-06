from usuarios_base_datos import usuarios
from crud_dispositivos import listar_dispositivos

def usuario_estandar(mail):
    
    while True:
        print("\n")
        print("1 Datos Personales")
        print("2 Control dispositivos")
        print("3 Dispositivos disponibles")
        print("4 Salir \n")
        
        opcion=int(input("ingrese una opcion: "))

        if opcion== 1:
            for usuario in usuarios:
                if mail == usuario["email"]:
                    rol="Administrador" if usuario["es_admin"] else "Usuario"

                    print("-------------------- Datos personales--------------------")

                    print(f"- nombre : {usuario["nombre"]}")
                    print(f"- apellido: {usuario["apellido"]}")
                    print(f"- email: {usuario['email']}" )
                    print(f"- rol:{rol}")
                    
                    
                    print("---------------------------------------------------------")
                 

        if opcion == 2:
            pass

        if opcion == 3:
            listar_dispositivos()

        if opcion == 4:
            break


        
        

