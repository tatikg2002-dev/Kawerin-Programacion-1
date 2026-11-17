#Ordenamiento_rapido

def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)  

Esto = [3, 6, 8, 10, 1, 2, 11, 4, 5, 7, 9]

print(ordenamiento_rapido(Esto))