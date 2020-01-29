from collections import deque


def is_bipartite(G):
    color = [-1]*len(G)
    visited = [False]*len(G)
    Q = deque()
    Q.append(0)
    visited[0] = True
    color[0] = 0
    while len(Q) > 0:
        curr = Q.popleft()
        for v in G[curr]:
            if color[v] != -1 and color[v] == color[curr]:
                return False
            color[v] = 1-color[curr]
            if visited[v] is False:
                Q.append(v)
                visited[v] = True
    return True
                

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

    print(G)
    print(is_bipartite(G))

if __name__ == '__main__':
    main()