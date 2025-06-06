from usuarios_base_datos import usuarios
from main import dispo

def listar_usuarios():
     for usuario in usuarios:
        rol="Administrador" if usuario["es_admin"] else "Usuario"
                    
        print("---------------------------------------------------------")

        print(f"- nombre : {usuario["nombre"]}")
        print(f"- apellido: {usuario["apellido"]}")
        print(f"- email: {usuario['email']}" )
        print(f"- rol: {rol}\n")

def cambio_rol(mail):
    for usuario in usuarios:
                if mail == usuario["email"]:
                    usuario["es_admin"] = True
                if mail != usuario["email"] and usuario["es_admin"] == True:
                    usuario["es_admin"] = False

def usuario_administrador():
    while True:
        print("\n")
        print("1 Consultar automatizaciones activas")
        print("2 Gestionar dispositivos")
        print("3 Modificar el rol de un usuario")
        print("4 Salir \n")
                
        opcion=int(input("ingrese una opcion: "))
        
        if opcion == 1:
            pass 
        if opcion == 2:
            dispo() 
        if opcion == 3:
            listar_usuarios()
            mail=input("ingresar el mail del usaurio: ")
            cambio_rol(mail)
        if opcion == 4:
            break
