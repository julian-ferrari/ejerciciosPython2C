def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''

    '''
    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}

    for origen, destino in aristas:
        grados[origen] += 1
        grados[destino] += 1

    return grados
    '''

    vertices, aristas = grafo_lista
    grados = {}

    for v in vertices:
        grados[v] = 0
    for a, b in aristas:
        grados[a] += 1
        grados[b] += 1

    return grados


def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    grados = cuenta_grado(grafo_lista)
    aislados = []

    for v in grados:
        if (grados[v] == 0):
            aislados.append(v)
    
    return aislados

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    nodos, aristas = grafo_lista

    grafo = {}
    for nodo in nodos:
        grafo[nodo] = []

    for a, b in aristas:
        grafo[a].append(b)
        grafo[b].append(a)

    visitados = []
    componentes = []

    for nodo in nodos:
        if nodo not in visitados:
            componente = []
            cola = [nodo]
            while len(cola) > 0:
                actual = cola.pop(0)
                if actual not in visitados:
                    visitados.append(actual)
                    componente.append(actual)
                    for vecino in grafo[actual]:
                        if vecino not in visitados and vecino not in cola:
                            cola.append(vecino)
            componentes.append(componente)

    return componentes

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1

def es_completo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, devuelve True/False si el grafo es o no completo.
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B A', 'A C', 'C A', 'B C', 'C B']
    Ejemplo formato salida:
    	True
    '''
    vertices, aristas = grafo_lista
    n = len(vertices)
    e = len(aristas)

    max_aristas = ((n * (n+1)) / 2)

    return e == max_aristas
    	
def aristas_de(grafo, vertice):
    '''
    Dado un grafo en representacion de lista, devuelva todas las aristas salientes desde un vértice dado
    Ejemplo Entrada:
    	grafo = ['3', 'A', 'B', 'C', 'A B', 'A C', 'B C']
	aristas_de(grafo, 'A')
    Ejemplo formato salida:
    	[('A', 'B'), ('A', 'C')]
    '''
    vertices, aristas = grafo
    
    return [arista for arista in aristas if arista[0] == vertice]

def grafo_inducido(grafo, subconjunto_vertices):
    '''
    Dado un grafo en representacion de lista, y un subconjunto de vertices,
    devuelva el subgrafo inducido
    Ejemplo Entrada:
    	grafo = ['4', 'A', 'B', 'C', 'D', 'A B', 'A C', 'B D']
	subconjunto_vertices = ['A', 'B', 'C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'B'), ('A', 'C')])
    '''
    vertices, aristas = grafo
    
    aristas_inducidas = [arista for arista in aristas if arista[0] in subconjunto_vertices and arista[1] in subconjunto_vertices]
    return (subconjunto_vertices, aristas_inducidas)

def grafo_complementario(grafo):
    '''
    Dado un grafo en representacion de lista, devuelve el grafo complementario en forma de lista
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B')])
    '''
    vertices, aristas = grafo
    aristas_set = set(aristas)

    complemento_aristas = []

    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            v1 = vertices[i]
            v2 = vertices[j]
            if (v1, v2) not in aristas_set and (v2, v1) not in aristas_set:
                complemento_aristas.append((v1, v2))

    return (vertices, complemento_aristas)
