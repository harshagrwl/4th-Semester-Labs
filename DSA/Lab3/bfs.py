from collections import deque
class Graph:
    def __init__(self,G):
        self.adjList = [x[:] for x in G]
        self.numV = len(G)

    def bfsutil(self,start):
        self.distance[start] = 0
        self.color[start] = 1
        q = deque()
        q.append(start)
        while len(q) > 0:
            n = q.popleft()
            for v in self.adjList[n]:
                if self.color[v] is False:
                    q.append(v)
                    self.color[v] = True
                    self.parent[v] = n
                    self.distance[v] = self.distance[n] + 1
            print("Current node ", n, "  distance : ", self.distance[n])


    def bfs(self,start):
        self.color = [False for x in range(self.numV)]
        self.distance = [10 for x in range(self.numV)]
        self.parent = [None for x in range(self.numV)]
        self.bfsutil(start)

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()

    s = int(input("Enter the source "))
    graph = Graph(G)
    graph.bfs(s)  

if __name__ == '__main__':

    main()