from collections import deque

def bfs(source,G):
    nodes = [{'visited' : False,'distance' : -1,'adj_nodes' : G[i],'prev' : None} for i in range(len(G))]
    Q = deque()
    Q.append(source)
    nodes[source]['visited'] = True
    nodes[source]['distance'] = 0
    while len(Q) > 0:
        curr = Q.popleft()
        for v in nodes[curr]['adj_nodes']:
            if nodes[v]['visited'] is False:
                Q.append(v)
                nodes[v]['visited'] = True
                nodes[v]['distance'] = nodes[curr]['distance'] + 1
                nodes[v]['prev'] = curr
        print("Current node ", curr,' distance (',nodes[curr]['distance'],')')

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

    #print(G)
    s = int(input("Enter the source "))
    bfs(s,G)

if __name__ == '__main__':
    main()