import math


def create(v1,v2):
	adjlist[v1].append(v2)
	adjlist[v2].append(v1)
	adjmatrix[v1][v2] = 1
	adjmatrix[v2][v1] = 1

def print1():
	print("adjlist: ")
	for i in range(v):
		print("Vertex ",i,": ",end=" ")
		for j in range(len(adjlist[i])):
			print(adjlist[i][j],end=" ")
		print()

	print("adjmatrix: ")
	for i in range(v):
		for j in range(v):
			print(adjmatrix[i][j],end=" ")
		print()

v = int(input('Enter the no. of vertices: '))
e = int(input('Enter the no of edges: '))
adjlist = [[] for i in range(v)]
adjmatrix = [[0 for i in range(v)] for i in range(v)]
for _ in range(e):
	v1,v2 = input().split()
	create(int(v1),int(v2))
print1()
	
