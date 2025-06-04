from dispositivos import dispositivos

def listar_dispositivos():

    if dispositivos:

        print("Dispositivos disponibles: ")

        for nombre in dispositivos.keys():
            print(f"  - {nombre} ")

    else:

        print("No hay dispositivos disponibles")


def buscar_dispositivos(nombre_dispositivo):
    listar_dispositivos()
    if nombre_dispositivo in dispositivos:
       
       return f"el dispositivos{nombre_dispositivo} fue encontrado"
    else:
        return f"el dispositivos{nombre_dispositivo} no fue encontrado"
    
    
def agregar_dispositivos(nuevo_dispositivo):

    if  nuevo_dispositivo in dispositivos:
       return "ya se encuentra este dispositivo "
    else:
        dispositivos[nuevo_dispositivo]={"datos":"dato"}

    listar_dispositivos()

    

def eliminar_dispositivos(dispositivo_eliminado):
     
    if dispositivo_eliminado in dispositivos:
        del dispositivos[dispositivo_eliminado]
        print(f"Dispositivo '{dispositivo_eliminado}' eliminado exitosamente.")
    else:
        print(f"El dispositivo '{dispositivo_eliminado}' no fue encontrado.")
    
    listar_dispositivos()

