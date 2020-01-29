class Graph:
    def __init__(self, G):
        self.adjList = [x[:] for x in G]
        self.numV = len(G)
        self.hash = {}
        for a in range(len(self.adjList)):
            for b in self.adjList[a]:
                self.hash[(min(a, b), max(a, b))] = "Back Edge"
    def dfs(self,start):
        self.visited[start] = True
        self.startTime[start] = self.time
        self.time += 1

        for v in self.adjList[start]:
            if self.visited[v] is False:
                self.parent[v] = start
                self.dfs(v)
                self.hash[(min(start,v), max(start,v))] = "Tree Edge"

        self.finishTime[start] = self.time
        self.time += 1

    def DFS_recursive(self, start = 0):
        self.visited = [False for x in range(self.numV)]
        self.startTime = [-1 for x in range(self.numV)]
        self.finishTime = [-1 for x in range(self.numV)]
        self.parent = [None for x in range(self.numV)]
        self.time = 0
        self.dfs(start)

        print("Start times of all the vertices: ",self.startTime)
        print("Finish times of all the vertices: ",self.finishTime)
        print("Parents of all the vertices: ",self.parent)
        print("The Edges of the graph are: ",self.hash)     

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

    graph = Graph(G)
    graph.DFS_recursive()    

if __name__ == '__main__':

    main()