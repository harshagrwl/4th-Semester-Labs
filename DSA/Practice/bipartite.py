from collections import deque

def create(v1,v2):
    adjlist[v1].append(v2)
    adjlist[v2].append(v1)
    adjmatrix[v1][v2] = 1
    adjmatrix[v2][v1] = 1

def bfs(node):
    q = deque([node])
    vis[node] = True
    while q:
        top = q.popleft()
        print(top,end=" ")
        for i in adjlist[top]:
            if vis[i] == False:
                dis[i] = dis[top]+1
                q.append(i)
                vis[i] = True
                
            else:
                if dis[i] == dis[top]:
                    flg = 1

v = int(input('Enter the no. of vertices: '))
e = int(input('Enter the no of edges: '))
adjlist = [[] for i in range(v)]
adjmatrix = [[0 for i in range(v)] for i in range(v)]
for _ in range(e):
    v1,v2 = input().split()
    create(int(v1),int(v2))

vis = [False]*v
dis = [0 for i in range(100)]
flg = 0
for i in range(len(adjlist)):
    if vis[i] == False:
        bfs(i)
        
if flg==1:
    print("The graph is  non Bipartite")
elif flg==0:
    print("The graph is bipartite")
