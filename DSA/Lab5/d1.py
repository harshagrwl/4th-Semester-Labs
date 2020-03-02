from collections import defaultdict
from heapq import *
def dijkstra(g, f, t):
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


    ''' Adjacency List representation. G is a list of lists. '''
G = []

file=open('input.txt','r')
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

print(G)
print(dijkstra(G,0,3))