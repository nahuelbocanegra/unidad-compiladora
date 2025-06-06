from dispositivos import dispositivos

def cambiar_estado(nombre, nuevo_estado=False):
    if nombre in dispositivos:
        dispositivos[nombre]["estado"] = nuevo_estado
        print(f"'{nombre}' ahora está {'encendido' if nuevo_estado else 'apagado'}.")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")

def modificar_dispositivo(nombre, **kwargs):
    if nombre in dispositivos:
        dispositivos[nombre].update(kwargs)
        print(f"'{nombre}' actualizado: {kwargs}")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")

def consultar_estado(nombre):
    if nombre in dispositivos:
        print(f"Estado de '{nombre}':")
        for clave, valor in dispositivos[nombre].items():
            print(f"  {clave}: {valor}")
    else:
        print(f"Dispositivo '{nombre}' no encontrado.")
