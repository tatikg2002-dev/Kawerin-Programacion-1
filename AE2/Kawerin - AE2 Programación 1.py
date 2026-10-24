# Kawerin Grieco Lautaro 44.406.777

cuentas_banco = [
    {"ID": 120210, "nombre": "Lautaro Kawerin Grieco", "saldo": 50000.0},
    {"ID": 120211, "nombre": "Juan Perez", "saldo": 50000.0},
    {"ID": 120212, "nombre": "Maria Gomez", "saldo": 50000.0},
    {"ID": 120213, "nombre": "Pedro Rodriguez", "saldo": 50000.0},
    {"ID": 120214, "nombre": "Ana Martínez", "saldo": 50000.0}
]

def buscar_cuenta():
    choice = input("Ingrese el nombre o ID de la cuenta: ").strip()
    if choice.isdigit():
        return consultar_cuenta_ID(int(choice))
    return consultar_cuenta_nombre(choice)

def consultar_cuenta_nombre(cuenta_nombre:str):
    for cuenta in cuentas_banco:
        if cuenta["nombre"] == cuenta_nombre.title():
            return cuenta   
    print("No se encontró la cuenta con el nombre proporcionado.")

def consultar_cuenta_ID(cuenta_id:int):
    for cuenta in cuentas_banco:
        if cuenta["ID"] == cuenta_id:
            return cuenta
    print("No se encontró la cuenta con el ID proporcionado.")

def tipo_operacion(operacion:int, monto:float):
    if operacion == 1:
        return abs(monto)
    elif operacion == 2:
        return -abs(monto)
    else:
        print("Operación inválida. Por favor, ingrese 1 para depositar o 2 para extraer dinero.")
        return 0

def modificar_dinero(cuenta:dict, monto:float):    
    if monto < 0 and cuenta["saldo"] < abs(monto):
        print("Error: fondos insuficientes. No se realizó la operación.")
        return
    cuenta["saldo"] = cuenta["saldo"] + monto
    print(f"Operación realizada con éxito. Nuevo saldo: ${cuenta['saldo']:,.2f}")    


def registrar_cuenta():
    nuevo_ID = cuentas_banco[-1]["ID"] + 1
    nuevo_nombre = input("Ingrese el nombre del cliente: ").strip().title()
    if nuevo_nombre:
        nueva_cuenta = {"ID": nuevo_ID, "nombre": nuevo_nombre, "saldo": 50000.0}
        cuentas_banco.append(nueva_cuenta)
        print(f"Se ha creado una nueva cuenta con ID: {nuevo_ID} y saldo inicial de $50,000.00")
    else:
        print("Debe ingresar un nombre con tal de registrarse")

cuenta = None
operacion = None
monto = None
monto_modificado = None
opcion = 0
while opcion != 4:
    print("CAJERO AUTOMATICO")
    print("1 - Consultar saldo disponible")
    print("2 - Depositar o extraer dinero")
    print("3 - Registrar nueva cuenta")
    print("4 - Salir del sistema")
    
    opcion = (input("Seleccione una opción: "))

    if not opcion.isdigit():
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 4:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
        
    match opcion:
        case 1:
            cuenta = buscar_cuenta()
            if cuenta:
                print(f"El saldo de {cuenta['nombre']} es de ${cuenta['saldo']:,.2f}")

        case 2:
            cuenta = buscar_cuenta()
            if cuenta:
                operacion = input("Ingrese 1 para depositar o 2 para extraer dinero: ")
                if not operacion.isdigit():
                    print("Entrada inválida. Debe ingresar 1 o 2.")
                    continue
                operacion=int(operacion)
            
                monto = input("Ingrese el monto: ").strip()
                if not monto.replace(".", "", 1).isdigit():
                    print("Entrada inválida. Debe ingresar un número positivo.")
                    continue
                monto=float(monto)

                if monto <= 0:
                    print("El monto debe ser mayor a 0.")
                    continue

                monto_modificado = tipo_operacion(operacion, monto)
                if monto_modificado != 0:
                    modificar_dinero(cuenta, monto_modificado)
        case 3:
            registrar_cuenta()
        case 4:
            print("Saliendo del sistema...")
      
    print("\n") 
