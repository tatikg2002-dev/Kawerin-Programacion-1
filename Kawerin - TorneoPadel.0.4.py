# Aplicar técnicas de ordenación interna sobre los datos del torneo
# con los métodos de Selección y Burbuja. Reconocer cómo cambia el resultado según
# el criterio de ordenamiento y comparar el trabajo que hace cada método.

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
            "jugador_2": dos_lugares[1],
            "puntos": 0
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

def ordenar_alfabetico(lista_original:list):
    lista=lista_original[:]
    n = len(lista)
    for i in range(n-1):
        posicion_menor = i
        for j in range(i+1,n):
            comparaciones_a = comparaciones_a + 1
            if lista[j]["nombre"].lower() < lista[posicion_menor]["nombre"].lower():
                posicion_menor=j

        if posicion_menor != i:
            lista[i], lista[posicion_menor] = lista[posicion_menor], lista[i]
            intercambios_a = intercambios_a + 1

    return lista

def mostrar_alfabetico():
    inscriptos = leer_json("lista_torneo.json")
    ordenada = ordenar_alfabetico(inscriptos)
    print("LISTA DE INSCRIPTOS")
    for jug in ordenada:
        print(f"{jug['nombre']} | Categoría: {jug['categoria']}")

def va_despues(a:dict,b:dict):
    if a["categoria"] != b["categoria"]:
        return a["categoria"] > b["categoria"]
    else:
        return a["nombre"].lower() > b["nombre"].lower()

def ordenar_categoria(lista_original:list):
    lista = lista_original[:]
    n = len(lista)
    i = 0
    hubo_intercambio = True
    comparaciones_b = 0
    intercambios_b = 0

    while i < n - 1 and hubo_intercambio:
        hubo_intercambio = False
        for j in range(n - 1 - i):
            comparaciones_b = comparaciones_b + 1
            if va_despues(lista[j], lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios_b = intercambios_b + 1
                hubo_intercambio = True
        i = i + 1

    return lista

def mostrar_cartelera():
    inscriptos = leer_json("lista_torneo.json")
    ordenada = ordenar_categoria(inscriptos)
    print("CARTELERA")
    categoria_actual = None
    for jug in ordenada:
        if jug["categoria"] != categoria_actual:
            categoria_actual = jug["categoria"]
            print(f"\n- Categoría {categoria_actual} -")
        print(f"  {jug['nombre']}")

def cargar_puntos_parejas():
    parejas = leer_json("lista_parejas.json")
    for i in range(len(parejas)):
        print(f"{i+1}) {parejas[i]['nombre_pareja']} - puntos actuales: {parejas[i]['puntos']}")
    
    opcion = int(input("Ingrese el número de la pareja: "))
    if opcion < 1 or opcion > len(parejas):
        print("Número de pareja inválido")

    puntos_texto = input("Ingrese los puntos que gano la pareja: ").strip()  
    parejas[opcion - 1]["puntos"] = parejas[opcion - 1]["puntos"] + int(puntos_texto)

    escribir_json("lista_parejas.json", parejas) 

def ordenar_posiciones(lista_original:list):
    lista = lista_original[:]
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["puntos"] < actual["puntos"]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = actual
    return lista

def mostrar_tabla_posiciones():
    parejas = leer_json("lista_parejas.json")
    parejas_ordenadas= ordenar_posiciones(parejas)
    print("TABLA DE POSICIONES")
    for i in range(len(parejas_ordenadas)):
        print(f"{i+1}º  {parejas_ordenadas[i]['nombre_pareja']} ({parejas_ordenadas[i]['jugador_1']['nombre']} / {parejas_ordenadas[i]['jugador_2']['nombre']}) - {parejas_ordenadas[i]['puntos']} pts")

def tabla_análisis():
    inscriptos = leer_json("lista_torneo.json")
    print(f"Cantidad de inscriptos: {len(inscriptos)}\n")
    print(f"{'Pedido':<10}{'Método':<10}{'Comparaciones':<10}{'Intercambios':<10}")
    print(f"{'1. Orden alfabético':<10}{'Selección':<10}{comparaciones_a:<10}{intercambios_a:<10}")
    print(f"{'2. Por categoría':<10}{'Burbuja':<10}{comparaciones_b:<10}{intercambios_b:<10}")

ok:int=-1
while ok != 0:
    print("\n")
    print("Menú de opciones")
    print("Agregar un nuevo jugador a la lista de inscriptos (1)")
    print("Mostrar la lista completa de inscriptos, en orden de inscripción (2)")
    print("Buscar un jugador por nombre (3)")
    print("Eliminar un jugador de la lista (4)")
    print("Mostrar lista de inscriptos en orden alfabetico (5)")
    print("Mostrar cartelera por categorias (6)")
    print("Cargar puntaje de pareja (7)")
    print("Mostrar tabla de posiciones (8)")
    print("Análisis metodos utilizados en 5 y 6 (9)")
    print("Salir del programa (0)")
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
            encontrado = buscar_jug(nombre_buscar)
            print(encontrado)
        case 4: 
            nombre_eliminar=str(input("Ingrese el nombre del jugador a eliminar: "))
            eliminar_jug(nombre_eliminar)
        case 5:
            comparaciones_a:int=0
            intercambios_a:int=0
            mostrar_alfabetico()
        case 6: 
            comparaciones_b:int=0
            intercambios_b:int=0
            mostrar_cartelera()
        case 7:
            cargar_puntos_parejas()
        case 8:
            mostrar_tabla_posiciones()
        case 9:
            tabla_análisis()