dispositivos = {
        "microondas": {
            "tipo": "Microondas con grill",
            "marca": "Panasonic",
            "modelo": "NN-GT68KS",
            "estado":False
        },
        "aire acondicionado": {
            "tipo": "Split Inverter",
            "marca": "LG",
            "modelo": "DualCool Artcool",
            "temperatura media": 20,
            "estado":False
        },
        "cafetera": {
            "tipo": "Cafetera espresso automática",
            "marca": "De'Longhi",
            "modelo": "Magnifica S ECAM 22.110.B",
            "estado":False
        }
}


def subir_temperatura_aire():
    
    temperatura=dispositivos["aire acondicionado"]["temperatura media"]
    
    if temperatura < 32:
        temperatura +=1
        print(f"Temperatura aumentada a {temperatura}°C")
    if temperatura >=32:
        return "La temperatura ya esta al maximo (32ºC)"

def bajar_temperatura_aire():

    temperatura=dispositivos["aire acondicionado"]["temperatura media"]
    if temperatura > 15:
        temperatura -= 1
        print(f"Temperatura disminuida a {temperatura}°C")
    if temperatura <= 15:
        return "La temperatura ya esta al minimo (15ºC)"

def controlar_aire():
   

    while True:

        print("Aire acondicionado")
        print(" 1- Subir temperatura \n " \
              "2- Bajar temperatura \n" \
              "3- Volver al menu principal  ")
        
        try:

            opcion=int(input("Elija una opcion: "))

            if opcion == 1 :
                subir_temperatura_aire()
            elif opcion == 2 : 
                bajar_temperatura_aire()
            elif opcion == 3:
                break
            else:
               print("Por favor, seleccione una opción válida (1, 2 o 3)")

        except:

            print("Entrada no valida,por favor ingrese un numero del (1, 2 o 3)")
