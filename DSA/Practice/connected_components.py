from collections import deque

def create(v1,v2):
	adjlist[v1].append(v2)
	adjlist[v2].append(v1)
	adjmatrix[v1][v2] = 1
	adjmatrix[v2][v1] = 1

def bfs(node):
	q = deque([node])
	vis[node] = count
	while q:
		top = q.popleft()
		#print(top,end=" ")
		for i in adjlist[top]:
			if vis[i] == 0:
				q.append(i)
				vis[i] = count

v = int(input('Enter the no. of vertices: '))
e = int(input('Enter the no of edges: '))
adjlist = [[] for i in range(v)]
adjmatrix = [[0 for i in range(v)] for i in range(v)]
for _ in range(e):
	v1,v2 = input().split()
	create(int(v1),int(v2))

vis = [0]*v
count = 1
for i in range(len(adjlist)):
	if vis[i] == 0:
		bfs(i)
		count += 1
print('total no of componenets: ',count-1)
for i in vis[0:len(adjlist)]:
	print(i,end=" ")