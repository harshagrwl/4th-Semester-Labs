import math
import heapq

def reverseg(G):
    Gr = [[] for i in range(len(G))]
    for u in range(len(G)):
        for v,w in G[u]:
            Gr[v].append((u,w))
    return Gr

def dijkstra(G,s):
    numvert = len(G)
    dis = [math.inf for x in range(numvert)]
    dis[s] = 0

    distnod = []
    for x in range(numvert):
        distnod.append((dis[x],x))
    heapq.heapify(distnod)

    while len(distnod):
        temp, u = heapq.heappop(distnod)

        if temp!= dis[u]:
            continue

        for v,w in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(distnod, (dis[v],v))

    print(dis)

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
    #Gr = reverseg(G)
    dijkstra(G,0)

if __name__ == '__main__' :
        main()