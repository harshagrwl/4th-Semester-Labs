class DSU:
    
    def __init__(self, num):
        self.parent = [x for x in range(num)]
        self.rank = [1 for x in range(num)]

    def findset(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.findset(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        a = self.findset(a)
        b = self.findset(b)
        
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        elif self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[min(a, b)] = max(a, b)
            self.rank[max(a, b)] += 1

class WeightedGraph:

    def __init__(self, G):
      self.adjacencyList = [x[:] for x in G]
      self.numVert = len(G)

    def dijkstra(self, s):
        import math
        import heapq

        self.distance = [math.inf for x in range(self.numVert)]
        self.distance[s] = 0

        self.dist_nod = []
        for i in range(self.numVert):
            self.dist_nod.append((self.distance[i], i))
        heapq.heapify(self.dist_nod)

        while len(self.dist_nod):
            temp, u = heapq.heappop(self.dist_nod)

            if temp != self.distance[u]:
                continue

            for v, weight in self.adjacencyList[u]:
                if self.distance[v] > self.distance[u] + weight:
                    self.distance[v] = self.distance[u] + weight
                    heapq.heappush(self.dist_nod, (self.distance[v], v))

    def prims(self):
        import math
        import heapq

        self.cost = [math.inf for x in range(self.numVert)]
        self.parent = [-1 for x in range(self.numVert)]
        self.cost[0] = 0
        self.tree = []

        self.cost_nod = []
        for i in range(self.numVert):
            self.cost_nod.append((self.cost[i], i))
        heapq.heapify(self.cost_nod)

        while len(self.cost_nod):
            temp, u = heapq.heappop(self.cost_nod)
            
            if temp != self.cost[u]:
                continue

            if self.parent[u] != -1:
                self.tree.append((self.parent[u], u))

            for v, weight in self.adjacencyList[u]:
                if self.cost[v] >  weight:
                    self.cost[v] = weight
                    self.parent[v] = u
                    heapq.heappush(self.cost_nod, (self.cost[v], v))

    def kruskals(self):
        dsu = DSU(self.numVert)

        edges = []
        for u in range(self.numVert):
            for v, weight in self.adjacencyList[u]:
                edges.append((weight, u, v))
        edges.sort()

        self.tree = []

        for weight, u, v in edges:
            if dsu.findset(u) != dsu.findset(v):
                self.tree.append((u, v))
                dsu.union(u, v)

def main():
    G = []
    file=open('input1.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)
    file.close()

    g = WeightedGraph(G)
    g.dijkstra(0)
    print(g.distance)

if __name__ == '__main__' :
        main()
