#Ascensor
import time

def codigo_piso(piso):
    if piso == 0:
        return "PB"
    else:
        return str(piso)
    
def mover_ascensor(piso_actual, piso_destino):

    piso_actual_str = codigo_piso(piso_actual)
    piso_destino_str = codigo_piso(piso_destino)

    if piso_actual == piso_destino:
        print(f"Llegado a destino [{piso_actual_str}]")
        return
    time.sleep(0.5)
    print(f"Ascensor en piso [{piso_actual_str}]")

    if piso_actual < piso_destino:
        mover_ascensor(piso_actual + 1, piso_destino)
    else:
        mover_ascensor(piso_actual - 1, piso_destino)
        
mover_ascensor(0, 5)
print(" ")
mover_ascensor(5, 0)


    