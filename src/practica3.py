def dijkstra_hasta(grafo, origen, destino):
    """
    Algoritmo de Dijkstra que retorna tanto la distancia como el camino.
    
    Entrada:
        grafo: diccionario {vertice: [(adyacente, peso), ...]}
        origen: vértice inicial
        destino: vértice final
    
    Retorna:
        tupla (distancia, camino) donde:
        - distancia: distancia mínima (int/float) o float("inf") si no hay camino
        - camino: lista con el camino más corto, o [] si no hay camino
    """
    # Inicializar distancias
    distancias = {vertice: float("inf") for vertice in grafo}
    distancias[origen] = 0
    
    # Diccionario para reconstruir el camino
    predecessores = {vertice: None for vertice in grafo}
    
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
        
        # Si llegamos al destino, reconstruir y retornar el camino
        if vertice_actual == destino:
            camino = []
            actual = destino
            
            # Reconstruir camino desde destino hasta origen
            while actual is not None:
                camino.append(actual)
                actual = predecessores[actual]
            
            # Invertir para tener camino de origen a destino
            camino.reverse()
            
            return distancias[destino], camino
        
        # Actualizar distancias a vértices adyacentes
        for adyacente, peso in grafo[vertice_actual]:
            if adyacente not in visitados:
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[adyacente]:
                    distancias[adyacente] = nueva_distancia
                    predecessores[adyacente] = vertice_actual  # Guardar predecesor
    
    # Si no hay camino, retornar infinito y camino vacío
    return distancias[destino], []


# Ejemplo de uso
if __name__ == "__main__":
    grafo_ejemplo = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    distancia, camino = dijkstra_hasta(grafo_ejemplo, 'A', 'E')
    print(f"Distancia: {distancia}")
    print(f"Camino: {' -> '.join(camino)}")
    
    # Prueba sin camino
    grafo_desconectado = {
        'A': [('B', 1)],
        'B': [],
        'C': [('D', 1)],
        'D': []
    }
    
    distancia, camino = dijkstra_hasta(grafo_desconectado, 'A', 'C')
    print(f"Distancia A->C: {distancia}")
    print(f"Camino A->C: {camino}")