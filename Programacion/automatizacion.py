from dispositivos import dispositivos
from crud_dispositivos import cambiar_estado

def automatizar_luz(presencia):
    if presencia:
        cambiar_estado("luz", True)
        print("Presencia detectada. Luz encendida.")
    else:
        cambiar_estado("luz", False)
        print("Sin presencia. Luz apagada.")
