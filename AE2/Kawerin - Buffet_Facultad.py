import os
import json

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

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
    guardar_dia = {
        "Lunes": ventas[0],
        "Martes": ventas[1],
        "Miercoles": ventas[2],
        "Jueves": ventas[3],
        "Viernes": ventas[4]
    }
    archivo = open("ventas_semana.json", "w", encoding="utf-8")
    json.dump(guardar_dia, archivo, indent=4)
    archivo.close()

def registrar_venta(arreglo, catalogo):
    dia = str(input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")).capitalize()
    while dia not in dias_semana:
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

    fila:int = dias_semana.index(dia)
    arreglo[fila][columna] = arreglo[fila][columna] + cantidad
    print(f"Se ha registrado la venta de {cantidad} unidades del producto con código {id_producto} para el día {dia}.")

    guadar_ventas(arreglo)

def mostrar_informes(matriz, catalogo):

    print("\n INFORME SEMANAL" )
    
    print("\n * Unidades totales por producto:")
    max_unidades = -1
    producto_mas_vendido = []
    
    for j in range(6):
        total_prod = 0
        for i in range(5):
            total_prod = total_prod + matriz[i][j]
        
        print(f"~ {catalogo[j]['nombre']}: {total_prod} unidades.")
        
        if total_prod > max_unidades:
            max_unidades = total_prod
            prod_mas_vendidos = [catalogo[j]['nombre']]
        elif total_prod == max_unidades:
            prod_mas_vendidos.append(catalogo[j]['nombre'])
            
    print(" * Recaudación por día:")
    max_recaudacion = -1
    dia_mayor_recaudacion = "" #Arranca vacía, acá se va a guardar el nombre del día que más plata hizo
    recaudacion_total = 0
    
    for i in range(5):
        recaudacion_dia = 0
        for j in range(6):
            cantidad = matriz[i][j]
            precio = catalogo[j]["precio"]
            recaudacion_dia = recaudacion_dia + (cantidad * precio)
            
        print(f"- {dias_semana[i]}: ${recaudacion_dia}")
        recaudacion_total = recaudacion_total + recaudacion_dia
        
        if recaudacion_dia > max_recaudacion:
            max_recaudacion = recaudacion_dia
            dia_mayor_recaudacion = dias_semana[i]

    print("\n * Producto mas vendido y dia de mayores ventas:")

    mas_vendidos:str = " y ".join(producto_mas_vendido)
    print(f"- Producto más vendido: {mas_vendidos} ({max_unidades} unid.)")
    print(f"- Día de mayor recaudación: {dia_mayor_recaudacion} (${max_recaudacion})")
    
    print("\n * Productos sin ventas en la semana:")
    sin_ventas = False
    for j in range(6):
        vendido = False
        for i in range(5):
            if matriz[i][j] > 0:
                vendido = True
                break
        if not vendido:
            print(f"- {catalogo[j]['nombre']}")
            sin_ventas = True          
    if not sin_ventas:
        print("- Todos los productos tuvieron al menos una venta.")
        
    print(f"\n * Total de la semana: ${recaudacion_total}")

lista_catalogo = cargar_catalogo()
matriz_ventas = datos_ventas()

opcion = 0
while opcion != 3:
    print("\nMENÚ PRINCIPAL")
    print("1. Registrar venta")
    print("2. Mostrar informes semanales")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        registrar_venta(matriz_ventas, lista_catalogo)
    elif opcion == 2:
        mostrar_informes(matriz_ventas, lista_catalogo)
    elif opcion == 3:
        print("Cerrando el sistema...")
        guadar_ventas(matriz_ventas)
    else:
        print("Opción incorrecta")

