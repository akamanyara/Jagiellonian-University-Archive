import heapq

def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())  # wierzchołki
    edges = [list(map(int, line.strip().split())) for line in lines[1:]]
    
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))  # fraf skierowany
    
    return graph

def dijkstra(graph, start, end):
    heap = [(0, start)]  # (koszt, węzeł)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        if current_node == end:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
    
    if distances[end] == float('inf'):  # Brak ścieżki
        return None, []
    
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    
    return distances[end], path

graph = read_from_file("GrafD1.txt")

# Znalezienie najkrótszej ścieżki od węzła 1 do 12
cost, path = dijkstra(graph, 1, 12)

if path:
    print(f"Najkrótsza odległość z węzła 1 do węzła 12: {cost}")
    print(f"Ścieżka: {' -> '.join(map(str, path))}")
else:
    print("Brak dostępnej ścieżki między podanymi węzłami.")
