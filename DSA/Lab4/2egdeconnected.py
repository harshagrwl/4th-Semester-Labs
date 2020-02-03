class Graph:
    def __init__(self, G):
        self.adjList = [x[:] for x in G]
        self.numV = len(G)
        # self.treeEdge = []
        # self.backEdge = []
        
    def dfs(self,start):
        self.src = start
        self.visited[start] = True
        self.startTime[start] = self.time
        self.time += 1
        self.sst = self.startTime[start]
        for v in self.adjList[start]:
            if self.visited[v] is False:
                # self.parent[v] = start
                self.sst = min(self.dfs(v),self.sst)
                # self.treeEdge.append((min(start,v), max(start,v)))

            else:
                if self.startTime[v] >= self.startTime[start]:
                    self.sst = min(self.startTime[v],self.sst)

        if self.sst == self.startTime[start] and start != self.src:
            print("Not 2 Edge Connected")
            exit()
        print(self.sst)
        return self.sst
    def DFS_recursive(self, start = 0):
        self.visited = [False for x in range(self.numV)]
        self.startTime = [-1 for x in range(self.numV)]
        self.finishTime = [-1 for x in range(self.numV)]
        self.parent = [None for x in range(self.numV)]
        self.time = 0
        self.dfs(start)
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
    # s = int(input('Enter the source'))
    graph = Graph(G)
    graph.DFS_recursive()    

if __name__ == '__main__':

    main()