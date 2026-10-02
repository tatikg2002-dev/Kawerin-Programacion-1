# "Quiero guardar la lista de inscriptos y quiero poder agregar a esa lista algún nuevo inscripto en caso de ser necesario."
# "Cuando alguien pregunta si está anotado, quiero poder mostrar la lista completa sin tener que cargar todo de nuevo."
# "Quiero escribir el nombre de un jugador y saber si está inscripto y en qué categoría juega."
# "Si un jugador se lesiona y no puede jugar, quiero sacarlo de la lista."

import shutil

categorias = [8,7,6,5,4,3,2,1] # Las categorias de padle se jerarquizan de 8 a 1 de forma decendente

def cargar_lista(add:bool):
    with open("lista_torneo.txt","w") as f:
        nombreJ= str(input("Ingrese el nombre del jugador: "))
        while add:
            categoriaJ= int(input("Ingrese la categoria del jugador: "))
            if categoriaJ in categorias:
                break
            else:
                print("Ingrese una categoria correspondiente al sistema númerico de 8a a 1a categoria")
        f.write(f"{{\"numeroJugador\": {i+1}, \"nombre\": \"{nombreJ}\", \"categoria\": {categoriaJ}}}\n")

def mostrar_lista(lista):
    with open(lista,"r") as f:
        for linea in f:
            print(linea.strip())
    
def buscar_jug(nombre_buscar:str):
    checked=False
    with open("lista_torneo.txt","r") as f:
        for linea in f:
            if nombre_buscar == eval(linea.strip())["nombre"]:
                print(linea.strip())
                checked=True
        if not checked:
            print("El jugador no se encuentra registrado en el torneo")     

def eliminar_jug(nombre_eliminar:str):
    with open("lista_torneo.txt","r") as f:
        lineas=f.readlines()
    with open("lista_torneo.txt","w") as f:
        for linea in lineas:
            if nombre_eliminar != eval(linea.strip())["nombre"]:
                f.write(linea)
            else:
                print(f"El jugador {nombre_eliminar} ha sido eliminado de la lista de inscriptos")

with open("lista_torneo.txt","w") as f:
    for linea in f:
        jugadores_totales=int(input("¿Cuántos jugadores van a participar en el torneo? Ingrese el total: "))
        for i in range(jugadores_totales): # i no itera hasta el entero de no utilizar range(entero)
            nombreJ= str(input("Ingrese el nombre del jugador: "))
            while True:
                categoriaJ= int(input("Ingrese la categoria del jugador: "))
                if categoriaJ in categorias:
                    break
                else:
                    print("Ingrese una categoria correspondiente al sistema númerico de 8a a 1a categoria")
        f.write(f"{{\"numeroJugador\": {i+1}, \"nombre\": \"{nombreJ}\", \"categoria\": {categoriaJ}}}\n")

parejas_totales= int(jugadores_totales/2) # Por el momento tomemos que todo torneo tendra una cantidad par de participantes
shutil.copy("lista_torneo.txt","lista_pick.txt") # Requiero de una copia editable de los jugadores disponibles para conformar una pareja 
pick_jugadores = []

with open("lista_pick.txt", "r") as f:
    for linea in f:
        pick_jugadores.append(eval(linea.strip()))

dos_integrantes=[] # Para poder guardar los integrantes y cargarlos simultaneamente

with open("lista_parejas.txt","w") as f:
    for linea in f:
        for i in range(parejas_totales):
            nombre_pareja=str(input("Ingrese el nombre de la pareja a conformar: "))
            print(pick_jugadores) # Muestro por pantalla los jugadores sin pareja

            for j in range(2): # Solo pueden ser dos jugadores por pareja
                num_integrante=int(input(f"Ingresar intergrante N° {j+1} de [{nombre_pareja}] por numero de jugador en el torneo: "))
                for jug in eval(linea.strip()):
                    if jug["numeroJugador"] == num_integrante:
                        check_integrante=jug
                    break
            dos_integrantes.append(check_integrante["nombre"])
            pick_jugadores.remove(check_integrante)

        f.write(f"{{\"nombre\": \"{nombre_pareja}\", \"jugador1\": \"{dos_integrantes[0]}\", \"jugador2\": \"{dos_integrantes[1]}\"}}\n")

while ok:
    print("Agregar un nuevo jugador a la lista de inscriptos (1)\n")
    print("Mostrar la lista completa de inscriptos (2)\n")
    print("Buscar un jugador por nombre (3)\n")
    print("Eliminar un jugador de la lista (4)\n")
    print("Salir del programa (5)\n")
    opcion=int(input("Ingrese la opción deseada: "))
    if opcion==5:
        ok=False
    else:
        match opcion:
            case 1:
                cargar_lista(True)
            case 2:
                mostrar_lista("lista_torneo.txt")
            case 3:
                nombre_buscar=str(input("Ingrese el nombre del jugador a buscar: "))
                buscar_jug(nombre_buscar)
            case 4: 
                nombre_eliminar=str(input("Ingrese el nombre del jugador a eliminar: "))
                eliminar_jug(nombre_eliminar)


