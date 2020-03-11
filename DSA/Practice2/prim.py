import math
import heapq

def prims(G):
    numVert = len(G)
    cost = [math.inf for x in range(numVert)]
    parent = [-1 for x in range(numVert)]
    cost[0] = 0
    tree = []

    cost_nod = []
    for i in range(numVert):
        cost_nod.append((cost[i], i))
    heapq.heapify(cost_nod)

    while len(cost_nod):
        temp, u = heapq.heappop(cost_nod)
            
        if temp != cost[u]:
            continue

        if parent[u] != -1:
            tree.append((parent[u], u))

        for v, weight in G[u]:
            if cost[v] >  weight:
                cost[v] = weight
                parent[v] = u
                heapq.heappush(cost_nod, (cost[v], v))

    print(tree)


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

    # g = WeightedGraph(G)
    # g.dijkstra(0)
    # print(g.distance)
    prims(G)

if __name__ == '__main__' :
        main()