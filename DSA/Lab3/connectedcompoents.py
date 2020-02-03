from collections import deque
G = []
vis = [0 for i in range(100)]
count = [1]
def bfs(node):
    q=deque([node])
    vis[node]=count[0]
    while q:
        print(q[0],end=" ")
        top=q.popleft()
        for i in G[top]:
            if vis[i]==0:
                q.append(i)
                vis[i]=count[0]



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

        for i in range(0,len(G)):
            if(vis[i]==0):
                bfs(i)
                count[0]+=1
        print('total no of componenets: ',count[0]-1)
        for i in vis[0:len(G)]:
            print(i,end=" ")
            

if __name__ == '__main__':
    main()