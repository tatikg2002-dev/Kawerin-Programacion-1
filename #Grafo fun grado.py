#Grafo

Adyacencia = {
    "A": ["B","C"],
    "B": ["A","C", "D"],
    "C": ["A","B"],
    "D": ["B","E"],
    "E": ["C","D"],
}

def grado(vertice):
    return len(Adyacencia[vertice])

ver = input("Ingrese el vértice: ")
print(f"El grado del vértice {ver} es: {grado(ver)}")
