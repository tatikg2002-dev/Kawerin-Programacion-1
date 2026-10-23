# a) Ingreso de jugadores

# Al iniciar el programa, el sistema debe preguntarle al juez:
#  "¿Cuántos jugadores van a participar en el torneo?".
# A partir de esa respuesta, debe permitir registrar cada competidor, uno por
#  uno, con la siguiente información:
#   su nombre (con el que se lo identificará dentro del torneo), y
#   su categoría (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

# b) Armado de parejas

# Una vez cargados todos los jugadores, el sistema debe permitir formar las
#  parejas del torneo.
# Cada pareja debe tener:
#   Un nombre que la identifique dentro del torneo (por ejemplo,
#   "Los Tanos"), y exactamente 2 jugadores, elegidos entre los que ya fueron inscriptos.

categorias = [8,7,6,5,4,3,2,1] # Las categorias de padle se jerarquizan de 8 a 1 de forma decendente
listaTorneo = [] 
listaParejas = []

jugadoresTotales=int(input("¿Cuántos jugadores van a participar en el torneo? Ingrese el total: "))
for i in range(jugadoresTotales): # i no itera hasta el entero de no utilizar range(entero)
    nombreJ= str(input("Ingrese el nombre del jugador: "))
    while True:
        categoriaJ= int(input("Ingrese la categoria del jugador: "))
        if categoriaJ in categorias:
            break
        else:
            print("Ingrese una categoria correspondiente al sistema númerico de 8a a 1a categoria")
    listaTorneo.append({"numeroJugador": i+1, "nombre": nombreJ, "categoria": categoriaJ})

parejasTotales= int(jugadoresTotales/2) # Por el momento tomemos que todo torneo tendra una cantidad par de participantes
pickJugadores=listaTorneo.copy() # Requiero de una copia editable de los jugadores disponibles para conformar una pareja 
dosIntegrantes=[] # Para poder guardar los integrantes y cargarlos simultaneamente
for i in range(parejasTotales):
    nombrePareja=str(input("Ingrese el nombre de la pareja a conformar: "))
    print(pickJugadores) # Muestro por pantalla los jugadores sin pareja

    for j in range(2): # Solo pueden ser dos jugadores por pareja
        numIntegrante=int(input(f"Ingresar intergrante N° {j+1} de [{nombrePareja}] por numero de jugador en el torneo: "))
        for jug in pickJugadores:
            if jug["numeroJugador"] == numIntegrante:
                checkIntegrante=jug
                break
        dosIntegrantes.append(checkIntegrante["nombre"])
        pickJugadores.remove(checkIntegrante)

    listaParejas.append({"nombre": nombrePareja, "jugador1": dosIntegrantes[0], "jugador2": dosIntegrantes[1]})

print(listaParejas)