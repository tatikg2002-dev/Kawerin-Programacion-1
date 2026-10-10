# Utilizar archivos .json para guardar la lista de jugadores y sus categorias.
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
    json.dump(datos, f, ensure_ascii=False, indent=2)

def cargar_lista(num_carga:int):
    lista_jugadores:list = leer_json("lista_torneo.json").strip()
    for i in range(num_carga):
        nombre_J = str(input(f"Ingrese el nombre del jugador {i+1}: ")).strip()
        numeros = [j["numero_jugador"] for j in lista_jugadores]
        numero_actual:int = max(numeros, default=0)
        while True:
            categoria_J = int(input(f"Ingrese la categoría de {nombre_J} (8 a 1): "))
            if categoria_J in categorias:
                break
            else:
                print("Ingrese una categoría correspondiente al sistema numérico de 8a a 1a categoría")
        numero_actual += 1
        nuevo_jugador = {
            "numero_jugador": numero_actual,
            "nombre": nombre_J,
            "categoria": categoria_J,
            }
        lista_jugadores.append(nuevo_jugador)

    escribir_json("lista_torneo.json", lista_jugadores)

def cargar_parejas(num_carga:int):
    lista_jugadores:list = leer_json("lista_torneo.json")
    lista_parejas:list = leer_json("lista_parejas.json")
    jugadores_con_pareja = set()
    for pareja in lista_parejas:
        jugadores_con_pareja.add(pareja["jugador_1"]["nombre"])
        jugadores_con_pareja.add(pareja["jugador_2"]["nombre"])
    pick_jugadores = [j for j in lista_jugadores if j["nombre"] not in jugadores_con_pareja]

    for i in range(num_carga):
        nombre_pareja = str(input(f"Ingrese el nombre de la pareja {i+1}: ")).strip()
        dos_lugares=[]

        for j in range(2):
            check_integrante=None
            while check_integrante is None:
                for jug in pick_jugadores:
                    print(f"Nº: {jug['numero_jugador']} | Nombre: {jug['nombre']} | Categoría: {jug['categoria']}")
        
                num_integrante=int(input(f"Ingresar intergrante N° {j+1} de [{nombre_pareja}] por numero de jugador en el torneo: "))

                for jug in pick_jugadores:
                    if jug["numero_jugador"] == num_integrante:
                        check_integrante = jug
                        break

                if check_integrante is None:
                    print("El número ingresado no corresponde a ningún jugador disponible.")
                else:
                    dos_lugares.append(check_integrante)
                    pick_jugadores.remove(check_integrante)

        nueva_pareja = {
            "nombre_pareja": nombre_pareja,
            "jugador_1": dos_lugares[0],
            "jugador_2": dos_lugares[1]
        }
        lista_parejas.append(nueva_pareja)

    escribir_json("lista_parejas.json", lista_parejas)

def mostrar_lista(archivo:str):
    lector = leer_json(archivo)
    print(json.dumps(lector, indent=2, ensure_ascii=False))

def buscar_jug(nombre_buscar:str):
    lista_jugadores:list = leer_json("lista_torneo.json")
    check_jugador:list = [jug for jug in lista_jugadores if nombre_buscar.strip().lower() == jug["nombre"].strip().lower()]
    if check_jugador != []:
        return (json.dumps(check_jugador, indent=2, ensure_ascii=False))
    else:
        print("El jugador buscado no se encuentra registrado en el torneo")

def eliminar_jug(nombre_eliminar:str):
    lista_jugadores = leer_json("lista_torneo.json")
    eliminar_J:list = buscar_jug(nombre_eliminar)
    if eliminar_J:
        lista_jugadores = [jug for jug in lista_jugadores if nombre_eliminar.strip().lower() != jug["nombre"].strip().lower()]
        escribir_json("lista_torneo.json", lista_jugadores)
        print(f"El jugador {nombre_eliminar} ha sido eliminado de la lista de inscriptos")

ok:int=0
while ok != 5:
    print("\n")
    print("Menú de opciones")
    print("Agregar un nuevo jugador a la lista de inscriptos (1)")
    print("Mostrar la lista completa de inscriptos (2)")
    print("Buscar un jugador por nombre (3)")
    print("Eliminar un jugador de la lista (4)")
    print("Salir del programa (5)")
    ok=int(input("Ingrese la opción deseada: "))
    print("\n")

    match ok:
        case 1:
            while True:
                cantidad_cargar=int(input("Ingrese la cantidad de jugadores a cargar: "))
                control = cantidad_cargar % 2
                if control == 0:
                    break
                else:
                    print("Ingresar una cantidad de jugadores par \n")
            cargar_lista(cantidad_cargar)
            cargar_parejas(int(cantidad_cargar/2))
        case 2:
            mostrar_lista("lista_torneo.json")
        case 3:
            nombre_buscar=str(input("Ingrese el nombre del jugador a buscar: "))
            buscar_jug(nombre_buscar)
        case 4: 
            nombre_eliminar=str(input("Ingrese el nombre del jugador a eliminar: "))
            eliminar_jug(nombre_eliminar)