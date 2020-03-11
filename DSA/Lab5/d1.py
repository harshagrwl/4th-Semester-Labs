from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1 == t:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return (float("inf"), [])

if __name__ == "__main__":
    
    G = []

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        weights = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
            #adjacentVertices.append((int(weight)))
        G.append(adjacentVertices)
        
        # G.append(weights)

    file.close()

    print(G)
    # print(dijkstra(G,0,3))
    #print(G[0][1][0])

    edges = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            edges.append((i,G[i][j][0],G[i][j][1]))

    
    print (edges)
    print ("1 -> 4:")
    print (dijkstra(edges, 1, 4))
    print ("2 -> 3:")
    print (dijkstra(edges, 2, 3))

    ''' Adjacency List representation. G is a list of lists. '''
