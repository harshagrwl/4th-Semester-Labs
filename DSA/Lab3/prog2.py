from collections import deque

def conn_comps(G):
    sets = []
    nodes = [-1]*len(G)
    for i in range(len(G)):
        if nodes[i] == -1:
            nodes[i] = len(sets)
            sets.append([i])
            source = i
            visited = [False]*len(G)
            Q = deque()
            Q.append(source)
            visited[source] = True
            while len(Q) > 0:
                curr = Q.popleft()
                for v in G[curr]:
                    if visited[v] is False:
                        Q.append(v)
                        visited[v] = True
                        nodes[v] = nodes[source]
                        sets[nodes[source]].append(v)
    print(sets)
            

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input2.txt','r')
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

    #print(G)
    conn_comps(G)

if __name__ == '__main__':
    main()