from usuario_estandar import usuario_estandar;
from usuario_administrador import usuario_administrador;
from usuarios_base_datos import usuarios;

def login():
    
    nombre=input("- Ingrese su nombre: ")
    apellido=input("- Ingrese su apellido: ")
    email=input("- Ingrese su mail: ")
    contrasena=input("- Ingrese una contraseña: ")
    es_administrador=False

    if len(usuarios) == 0:
        es_administrador = True
        

    if autenticacion(email) :
        
        print("El usuario ya esta registrado")

        return inicio()
    else:
        
        print(f"Usuario registrado, Bienvenido {nombre} ")
       
        usuarios.append({
            "nombre":nombre,
            "apellido":apellido,
            "email":email,
            "contrasena":contrasena,
            "es_administrador":es_administrador
        })

        return inicio()
    
def autenticacion(email):

    for usuario in usuarios:
        if email == usuario["email"]:
            return True
    return False
        
        
def inicio():

    email=input("ingrese su mail: ")
    contrasena=input("ingrese su contraseña: ")

    for usuario in usuarios:

        if email == usuario["email"] and contrasena == usuario["contrasena"]:

            if usuario["es_admin"] :

                return usuario_administrador()
            
            return usuario_estandar(email)
    

login()