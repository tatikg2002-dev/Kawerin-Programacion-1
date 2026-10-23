import os
import json

días_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

def cargar_catalogo(): 
    if os.path.exists("catalogo.json"):
        archivo = open("catalogo.json", "r", encoding="utf-8")
        catalogo = json.load(archivo)
        archivo.close()
        return catalogo
    else:
        catalogo = [
            {"codigo": 101, "nombre": "cafe con leche", "precio": 1500},
            {"codigo": 102, "nombre": "media luna", "precio": 700},
            {"codigo": 103, "nombre": "sandwich de miga", "precio": 1800},
            {"codigo": 104, "nombre": "agua mineral 500 ml", "precio": 1000},
            {"codigo": 105, "nombre": "empanada", "precio": 1200},
            {"codigo": 106, "nombre": "chipa (100 g)", "precio": 1300}
    ]
    archivo = open("catalogo.json", "w", encoding="utf-8")
    json.dump(catalogo, archivo, indent=4)
    archivo.close()
    return catalogo

def indice_producto(codigo_buscado, catalogo):
    for i in range(len(catalogo)):
        if catalogo[i]["codigo"] == codigo_buscado:
            return i
    return -1

def datos_ventas(): 
    ventas = []
    if os.path.exists("ventas_semana.json"):
        archivo = open("ventas_semana.json", "r", encoding="utf-8")
        datos_cargados = json.load(archivo)
        archivo.close()

        ventas.append(datos_cargados["Lunes"])
        ventas.append(datos_cargados["Martes"])
        ventas.append(datos_cargados["Miercoles"])
        ventas.append(datos_cargados["Jueves"])
        ventas.append(datos_cargados["Viernes"])
    else:
        ventas = [] 
        for f in range(5):
            fila = [0, 0, 0, 0, 0, 0] 
            ventas.append(fila)
    return ventas

def guadar_ventas(ventas): 
    guardar_día = {
        "Lunes": ventas[0],
        "Martes": ventas[1],
        "Miercoles": ventas[2],
        "Jueves": ventas[3],
        "Viernes": ventas[4]
    }
    archivo = open("ventas_semana.json", "w", encoding="utf-8")
    json.dump(guardar_día, archivo, indent=4)
    archivo.close()

def registrar_venta(arreglo, catalogo):
    dia = str(input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")).capitalize()
    while dia not in días_semana:
        print("Día inválido. Por favor, ingrese un día válido de la semana.")
        dia = str(input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")).capitalize()

    id_producto = int(input("Ingrese el código del producto: "))
    columna:int = indice_producto(id_producto, catalogo)
    while columna == -1:
        print("Código de producto inválido. Por favor, ingrese un código válido.")
        id_producto = int(input("Ingrese el código del producto: "))
        columna = indice_producto(id_producto, catalogo)

    cantidad = int(input("Ingrese la cantidad vendida: "))
    while cantidad <= 0:
        print("Cantidad inválida. Por favor, ingrese una cantidad mayor a cero.")
        cantidad = int(input("Ingrese la cantidad vendida: "))

    fila:int = dia - 1
    arreglo[fila][columna] = arreglo[fila][columna] + cantidad
    print(f"Se ha registrado la venta de {cantidad} unidades del producto con código {id_producto} para el día {dia}.")

    guadar_ventas(arreglo)

