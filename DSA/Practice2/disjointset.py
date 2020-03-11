import math

class disj:
	def __init__(self,num):
		parent = [x for x in range(num)]
		rank = [1 for x in range(num)]

	def findset(self,x):
		if parent[x] == x:
			return x

		parent[x] = findset(parent[x])
		return parent[x]

	def union(self,x,y):
		a = findset(x)
		b = findset(y)

		if rank[a] > rank[b]:
			parent[b] = a

		elif rank[b] > rank[a]:
			parent[a] = b

		else:
			parent[min(a,b)] = max(a,b)
			rank[max(a,b)] += 1

