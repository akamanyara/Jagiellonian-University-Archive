import heapq

def prim_mst(filename, start=6):
    with open(filename, 'r') as f:
        lines = f.readlines()

    n = int(lines[0])
    adj = [[] for _ in range(n)]

    for line in lines[1:]:
        u, v, w = map(int, line.split())
        adj[u].append((w, v))

    visited = [False] * n
    min_heap = [(0, start)]
    total_weight = 0
    visit_order = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = True
            total_weight += weight
            visit_order.append(u)
            for w, v in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        if len(visit_order) == n:
            break

    seventh_vertex = visit_order[6] if len(visit_order) > 6 else None
    return total_weight, seventh_vertex

filename = "Graf_Drzewo_MST_Algorytm_Prima.txt"
weight, seventh = prim_mst(filename)
print("Suma wag MST (Prim):", weight)
print("7. wierzchołek dodany do MST:", seventh)
