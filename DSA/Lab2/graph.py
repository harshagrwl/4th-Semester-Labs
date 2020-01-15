import math
class Graph:
    def __init__(self,nv):
        self.v = nv
        self.adjList = [[] for i in range(nv)]
        self.adjMatrix = [[0 for i in range(nv)] for i in range(nv)]

    def print(self):
        print("The Adjacency Matrix is: ")
        for i in range(self.v):
            for j in range(self.v):
                print(self.adjMatrix[i][j], end=' ')
            print()
        print("The Adjacency List is: ")
        for i in range(self.v):
            print("Vertex ", i ,":",end=' ')
            for j in range(len(self.adjList[i])):
                print(self.adjList[i][j], end=' ')
            print()

    def create(self,v1,v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1


n = Graph(int(input('Enter the number of vertices: ')))
p = int(input('Enter the number of Edges: '))
for _ in range(p):
    v1, v2 = input().split()
    n.create(int(v1),int(v2))
n.print()

