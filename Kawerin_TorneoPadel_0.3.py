# Utilizar archvos .json para guardar la lista de jugadores y sus categorias.
import json
import os

categorias = [8,7,6,5,4,3,2,1] 

def leer_json(archivo: str) -> list:
  if not os.path.exists(archivo):
    return []
  else:
    with open(archivo, "r", encoding="utf-8") as f:
      return json.load(f)

def escribir_json(archivo: str, datos: list):
  with open(archivo, "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_lista(num_carga:int):
    jugadores = leer_json("lista_torneo.json")
    for i in range(num_carga):
        nombreJ = str(input(f"Ingrese el nombre del jugador {i+1}: ")).strip()
        numeros = [j["numeroJugador"] for j in jugadores]
        numero_actual = max(numeros, default=0)
        while True:
            categoriaJ = int(input(f"Ingrese la categoría de {nombreJ} (8 a 1): "))
            if categoriaJ in categorias:
                break
            else:
                print("Ingrese una categoría correspondiente al sistema numérico de 8a a 1a categoría")
            numero_actual += 1
            nuevo_jugador = {
                "numeroJugador": numero_actual,
                "nombre": nombreJ,
                "categoria": categoriaJ,
                }
            jugadores.append(nuevo_jugador)

            escribir_json("lista_torneo.json", jugadores)
            
def cargar_parejas(num_carga:int):

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

    checked=False
    with open("lista_torneo.txt","r") as f:
        lineas = f.readlines()
    with open("lista_torneo.txt","w") as f:
        for linea in lineas:
            if nombre_eliminar != eval(linea.strip())["nombre"]:
                f.write(linea)
            else:
                checked=True
    if checked:
        print(f"El jugador {nombre_eliminar} ha sido eliminado del torneo")
    else:
        print("El jugador no se encuentra registrado en el torneo")

ok:int=0
while ok != 5:
    print("\n")
    print("Menu de opciones")
    print("Agregar un nuevo jugador a la lista de inscriptos (1)")
    print("Mostrar la lista completa de inscriptos (2)")
    print("Buscar un jugador por nombre (3)")
    print("Eliminar un jugador de la lista (4)")
    print("Salir del programa (5)")
    ok=int(input("Ingrese la opción deseada: "))

    match ok:
        case 1:
            while True:
                cantidad_cargar=int(input("Ingrese la cantidad de jugadores a cargar: "))
                control = cantidad_cargar % 2
                if control == 0:
                    break
                else:
                    print("Ingresar una cantidad de jugadores par ")
            cargar_lista(cantidad_cargar)
            cargar_parejas(int(cantidad_cargar/2))
        case 2:
            mostrar_lista("lista_torneo.txt")
        case 3:
            nombre_buscar=str(input("Ingrese el nombre del jugador a buscar: "))
            buscar_jug(nombre_buscar)
        case 4: 
            nombre_eliminar=str(input("Ingrese el nombre del jugador a eliminar: "))
            eliminar_jug(nombre_eliminar)