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

categorias = [8,7,6,5,4,3,2,1]
listaTorneo = []

jugadoresTotales=int(input("¿Cuántos jugadores van a participar en el torneo? Ingrese el total: "))
for i in range(jugadoresTotales):
    nombreJ= str(input("Ingrese el nombre del jugador: "))
    while True:
        categoriaJ= int(input("Ingrese la categoria del jugador: "))
        if categoriaJ in categorias:
            break
        else:
            print("Ingrese una categoria correspondiente al sistema númerico de 8a a 1a categoria")
    listaTorneo.append({"nombre": nombreJ, "categoria": categoriaJ})

print(listaTorneo)