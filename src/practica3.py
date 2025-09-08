def dijkstra_hasta(grafo, origen, destino):
    """
    Algoritmo de Dijkstra (versión básica sin cola de prioridad).
    Calcula la distancia mínima desde 'origen' hasta 'destino'.
    Entrada:
        grafo: diccionario {vertice: [(adyacente, peso), ...]}
        origen: vértice inicial
        destino: vértice final
    
    Retorna:
        distancia mínima (int/float) o float("inf") si no hay camino
    """
    # Inicializar distancias: infinito para todos los vértices excepto el origen
    distancias = {vertice: float("inf") for vertice in grafo}
    distancias[origen] = 0
    
    # Conjunto de vértices visitados
    visitados = set()
    
    while len(visitados) < len(grafo):
        # Encontrar el vértice no visitado con menor distancia
        vertice_actual = None
        distancia_minima = float("inf")
        
        for vertice in grafo:
            if vertice not in visitados and distancias[vertice] < distancia_minima:
                distancia_minima = distancias[vertice]
                vertice_actual = vertice
        
        # Si no hay vértice accesible, terminar
        if vertice_actual is None:
            break
            
        # Marcar como visitado
        visitados.add(vertice_actual)
        
        # Si llegamos al destino, retornar la distancia
        if vertice_actual == destino:
            return distancias[destino]
        
        # Actualizar distancias a vértices adyacentes
        for adyacente, peso in grafo[vertice_actual]:
            if adyacente not in visitados:
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[adyacente]:
                    distancias[adyacente] = nueva_distancia
    
    # Retornar la distancia al destino (puede ser infinito si no hay camino)
    return distancias[destino]


# Ejemplo de uso:
if __name__ == "__main__":
    # Grafo de ejemplo
    grafo_ejemplo = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    # Pruebas
    print(f"Distancia de A a E: {dijkstra_hasta(grafo_ejemplo, 'A', 'E')}")  # 8
    print(f"Distancia de A a D: {dijkstra_hasta(grafo_ejemplo, 'A', 'D')}")  # 7
    print(f"Distancia de B a E: {dijkstra_hasta(grafo_ejemplo, 'B', 'E')}")  # 7
    
    # Ejemplo sin camino
    grafo_desconectado = {
        'A': [('B', 1)],
        'B': [],
        'C': [('D', 1)],
        'D': []
    }
    
    print(f"Distancia de A a C: {dijkstra_hasta(grafo_desconectado, 'A', 'C')}")  # inf