class UndirGraph:

    def __init__(self, G):
        self.adjacencyList = [x[:] for x in G]
        self.numVert = len(G)

    def recDFS(self, startVertex):
        self.visited[startVertex] = True
        self.inTime[startVertex] = self.time
        self.time += 1

        for vert in self.adjacencyList[startVertex]:
            if not self.visited[vert]:
                self.parent[vert] = startVertex
                self.isTE[min(vert, startVertex), max(vert, startVertex)] = True
                self.recDFS(vert)

        self.outTime[startVertex] = self.time
        self.time += 1

    def DFS_recur(self, startVertex):
        self.visited = [False for x in range(self.numVert)]
        self.inTime = [-1 for x in range(self.numVert)]
        self.outTime = [-1 for x in range(self.numVert)]
        self.parent = [-1 for x in range(self.numVert)]
        self.time = 0

        self.isTE = {}
        for u in range(self.numVert):
            for v in self.adjacencyList[u]:
                self.isTE[min(u, v), max(u, v)] = False

        self.recDFS(startVertex)

        print("In times: ", self.inTime)
        print("Out times: ", self.outTime)
        print("Parents: ", self.parent)
        print("Edges: ", self.isTE)

    def DFS_iter(self, startVertex):
        visited = [False for x in range(self.numVert)]
        inTime = [-1 for x in range(self.numVert)]
        outTime = [-1 for x in range(self.numVert)]
        parent = [-1 for x in range(self.numVert)]
        time = 0

        isTE = {}
        for u in range(self.numVert):
            for v in self.adjacencyList[u]:
                isTE[min(u, v), max(u, v)] = False

        stack = [startVertex]
        while len(stack):
            vert = stack[-1]
            
            if visited[vert]:
                stack.pop()
                if outTime[vert] == -1:
                    outTime[vert] = time
                    time += 1
                continue

            visited[vert] = True
            inTime[vert] = time
            time += 1

            for v in self.adjacencyList[vert][::-1]:
                if not visited[v]:
                    parent[v] = vert
                    stack.append(v)

        for vert in range(self.numVert):
            if parent[vert] != -1:
                isTE[min(parent[vert], vert), max(parent[vert], vert)] = True

        print("In times: ", inTime)
        print("Out times: ", outTime)
        print("Parents: ", parent)
        print("Edges: ", isTE)

    def BFS(self, startVertex):
        from collections import deque

        self.visited = [0 for x in range(self.numVert)]
        self.level = [-1 for x in range(self.numVert)]
        self.parent = [-1 for x in range(self.numVert)]

        queue = deque()
        queue.append(startVertex)
        self.level[startVertex] = 0

        while len(queue):
            temp = queue.popleft()
                
            self.visited[temp] = 2

            for vert in self.adjacencyList[temp]:
                if self.visited[vert] == 0:
                    queue.append(vert)
                    self.visited[vert] = 1
                    self.level[vert] = self.level[temp] + 1
                    self.parent[vert] = temp

        print("Visited: ", self.visited)
        print("Level: ", self.level)
        print("Parent: ", self.parent)

    def recConn(self, startVertex):
        self.visited[startVertex] = True
        self.comp[startVertex] = self.count

        for vert in self.adjacencyList[startVertex]:
            if not self.visited[vert]:
                self.recConn(vert)

    def Connected(self):
        self.visited = [False for x in range(self.numVert)]
        self.comp = [-1 for x in range(self.numVert)]
        self.count = 0

        for vert in range(self.numVert):
            if not self.visited[vert]:
                self.recConn(vert)
                self.count += 1

        print("Comp: ", self.comp)
        
    def Bipartite(self):
        self.BFS(0)
        self.color = [-1 for x in range(self.numVert)]

        for u in range(self.numVert):
            for v in self.adjacencyList[u]:
                if self.visited[u] == 2 and self.visited[v] == 2:
                    if self.level[u] == self.level[v]:
                        print("Not Bipartite")
                        return

        for vert in range(self.numVert):
            if self.visited[vert] == 2:
                if self.level[vert]%2 == 0:
                    self.color[vert] = "Red"
                else:
                    self.color[vert] = "Black"
        
        print("Color: ", self.color)

    def rec2Edge(self, startVertex):
        self.visited[startVertex] = True
        self.inTime[startVertex] = self.time
        self.time += 1

        mine = self.inTime[startVertex]
        for vert in self.adjacencyList[startVertex]:
            if not self.visited[vert]:
                self.parent[vert] = startVertex
                mine = min(mine, self.rec2Edge(vert))
            elif vert != self.parent[startVertex]:
                mine = min(mine, self.inTime[vert])
        
        self.time += 1

        if mine == self.inTime[startVertex] and self.inTime[startVertex] != 0:
            mine = -1
        
        return mine

    def TwoEdge(self):
        self.visited = [False for x in range(self.numVert)]
        self.parent = [-1 for x in range(self.numVert)]
        self.inTime = [-1 for x in range(self.numVert)]
        self.time = 0

        if self.rec2Edge(0) == -1:
            print("Not 2 Edge Connected")
        else:
            print("2 Edge Connected")

        print("In times: ", self.inTime)
        print("Parents: ", self.parent)

    def recTopSort(self, startVertex):
        self.visited[startVertex] = self.count

        for vert in self.adjacencyList[startVertex]:
            if not self.visited[vert]:
                self.recTopSort(vert)
            elif self.visited[vert] == self.count:
                self.pos = False
        
        self.arr.append(startVertex)

    def TopSort(self):
        self.visited = [0 for x in range(self.numVert)]
        self.count = 1
        self.pos = True
        self.arr = []

        for vert in range(self.numVert):
            if not self.visited[vert]:
                self.recTopSort(vert)
                self.count += 1
            
        if self.pos:
            print(self.arr[::-1])
            
    def calcRev(self):
	    self.revAdjacencyList = [[] for x in range(self.numVert)]

	    for u in range(self.numVert):
		    for v in self.adjacencyList[u]:
			    self.revAdjacencyList[v].append(u)

    def SCC_DFSRev_Rec(self, startVertex):
	    self.revVisited[startVertex] = True

	    for vert in self.revAdjacencyList[startVertex]:
		    if not self.revVisited[vert]:
			    self.SCC_DFSRev_Rec(vert)

	    self.stack.append(startVertex)

    def SCC_DFSRev(self):
	    self.revVisited = [False for x in range(self.numVert)]

	    self.calcRev()

	    for vert in range(self.numVert):
		    if not self.revVisited[vert]:
			    self.SCC_DFSRev_Rec(vert)

    def SCC_DFS(self, startVertex, count):
	    self.visited[startVertex] = True
	    self.comp[startVertex] = count

	    for vert in self.adjacencyList[startVertex]:
		    if not self.visited[vert]:
			    self.SCC_DFS(vert, count)

    def findSCCs(self):
	    self.stack = []
	    self.SCC_DFSRev()
	    self.visited = [False for x in range(self.numVert)]
	    self.comp = [-1 for x in range(self.numVert)]

	    count = 0
	    for vert in self.stack[::-1]:
		    if not self.visited[vert]:
			    self.SCC_DFS(vert, count)
			    count += 1

	    print(count)
	    print(self.comp)

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    file=open('input3.txt','r')   
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

    graph = UndirGraph(G)
    graph.findSCCs()

if __name__ == '__main__':
    main()
