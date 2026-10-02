# "Quiero guardar la lista de inscriptos y quiero poder agregar a esa lista algún nuevo inscripto en caso de ser necesario."
# "Cuando alguien pregunta si está anotado, quiero poder mostrar la lista completa sin tener que cargar todo de nuevo."
# "Quiero escribir el nombre de un jugador y saber si está inscripto y en qué categoría juega."
# "Si un jugador se lesiona y no puede jugar, quiero sacarlo de la lista."

import shutil

categorias = [8,7,6,5,4,3,2,1] 


def cargar_lista(num_carga:int):
    for i in range(num_carga):
        nombreJ= str(input("Ingrese el nombre del jugador: "))
        while True:
            categoriaJ= int(input("Ingrese la categoria del jugador: "))
            if categoriaJ in categorias:
                break
            else:
                print("Ingrese una categoria correspondiente al sistema númerico de 8a a 1a categoria")
        with open("lista_torneo.txt","r") as f:
            numeros = [eval(linea.strip())["numeroJugador"] for linea in f if linea.strip()]
        numero = max(numeros, default=0) + 1
        with open("lista_torneo.txt","a") as f:
            f.write(f"{{\"numeroJugador\": {numero}, \"nombre\": \"{nombreJ}\", \"categoria\": {categoriaJ}}}\n")

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
        Revisado=f.readlines()
    with open("lista_torneo.txt","w") as f:
        for linea in Revisado:
            if nombre_eliminar != eval(linea.strip())["nombre"]:
                f.write(linea)
            else:
                print(f"El jugador {nombre_eliminar} ha sido eliminado de la lista de inscriptos")

while True:
    jugadores_totales=int(input("Ingrese la cantidad total de jugadores inscriptos: "))
    control = jugadores_totales % 2
    if control == 0:
        break
    else:
        print("Ingresar una cantidad de jugadores par ")
open("lista_torneo.txt","w").close()  
cargar_lista(jugadores_totales)

parejas_totales = int(jugadores_totales / 2) 
shutil.copy("lista_torneo.txt","lista_pick.txt") 
pick_jugadores = []

with open("lista_pick.txt", "r") as f:
    for linea in f:
        pick_jugadores.append(eval(linea.strip()))

dos_integrantes=[]

with open("lista_parejas.txt","w") as f:
    for i in range(parejas_totales):
        nombre_pareja=str(input("Ingrese el nombre de la pareja a conformar: "))
        print(pick_jugadores)

        for j in range(2):
            check_integrante=None
            while check_integrante is None:
                num_integrante=int(input(f"Ingresar intergrante N° {j+1} de [{nombre_pareja}] por numero de jugador en el torneo: "))
                for jug in pick_jugadores:
                    if jug["numeroJugador"] == num_integrante:
                        check_integrante=jug
                        break
            dos_integrantes.append(check_integrante["nombre"])
            pick_jugadores.remove(check_integrante)
        f.write(f"{{\"nombre\": \"{nombre_pareja}\", \"jugador1\": \"{dos_integrantes[0]}\", \"jugador2\": \"{dos_integrantes[1]}\"}}\n")

ok:int=0
while ok != 5:
    print("\n")
    print("Agregar un nuevo jugador a la lista de inscriptos (1)\n")
    print("Mostrar la lista completa de inscriptos (2)\n")
    print("Buscar un jugador por nombre (3)\n")
    print("Eliminar un jugador de la lista (4)\n")
    print("Salir del programa (5)\n")
    ok=int(input("Ingrese la opción deseada: "))

    match ok:
        case 1:
            cantidad_cargar=int(input("Ingresar la cantidad de jugadores a agregar: "))
            cargar_lista(cantidad_cargar)
        case 2:
            mostrar_lista("lista_torneo.txt")
        case 3:
            nombre_buscar=str(input("Ingrese el nombre del jugador a buscar: "))
            buscar_jug(nombre_buscar)
        case 4: 
            nombre_eliminar=str(input("Ingrese el nombre del jugador a eliminar: "))
            eliminar_jug(nombre_eliminar)


