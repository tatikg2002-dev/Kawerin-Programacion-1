#Integrantes: Kawerin Grieco Lautaro-44.406.777, Meza Soto Miguel Angel-42.222.984
# Saldo Inicial predeterminado
SALDO = 50000.0
OPCION = 0

while OPCION != 4:
    # Menú de Opciones
    print("CAJERO AUTOMATICO")
    print("1 - Consultar saldo disponible")
    print("2 - Depositar dinero")
    print("3 - Extraer dinero")
    print("4 - Salir del sistema")
    
    OPCION = int(input("Seleccione una opción: "))
    
    if OPCION == 1:
        print(f"Su saldo disponible es: ${SALDO}")
        
    elif OPCION == 2:
        monto = float(input("Ingrese el importe a depositar: "))
        if monto > 0:
            SALDO = SALDO + monto
            print("Depósito exitoso.")
        else:
            print("Error: El monto debe ser mayor a 0.")
            
    elif OPCION == 3:
        monto = float(input("Ingrese el importe a extraer: "))
        # Control de Extracciones (Validación)
        if monto <= SALDO:
            SALDO = SALDO - monto
            print("Extracción exitosa.")
        else:
            print("Fondos insuficientes para realizar la operación")
            
    elif opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("Opción inválida. Intente nuevamente.")
        
    print() # Salto de línea  para separar las operaciones