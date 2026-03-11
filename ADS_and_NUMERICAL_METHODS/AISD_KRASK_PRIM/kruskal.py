class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def kruskal_mst(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    n = int(lines[0])
    edges = set()
    
    for line in lines[1:]:
        u, v, w = map(int, line.split())
        if u < v:
            edges.add((w, u, v)) 

    edges = sorted(list(edges))
    uf = UnionFind(n)
    mst_weight = 0
    edge_count = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst_weight += w
            edge_count += 1
            if edge_count == n - 1:
                break

    return mst_weight

filename = "Graf_Drzewo_MST_Algorytm_Kruskala.txt"
print("Suma wag MST (Kruskal):", kruskal_mst(filename))
