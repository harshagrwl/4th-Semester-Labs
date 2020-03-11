import math

class disj:
	def __init__(self,num):
		self.parent = [x for x in range(num)]
		self.rank = [1 for x in range(num)]

	def findset(self,x):
		if self.parent[x] == x:
			return x

		self.parent[x] = self.findset(self.parent[x])
		return self.parent[x]

	def union(self,x,y):
		a = self.findset(x)
		b = self.findset(y)

		if self.rank[a] > self.rank[b]:
			self.parent[b] = a

		elif self.rank[b] > self.rank[a]:
			self.parent[a] = b

		else:
			self.parent[min(a,b)] = max(a,b)
			self.rank[max(a,b)] += 1


def kruskals(G):
	numvert = len(G)
	disjoint = disj(numvert)

	edges = []
	for u in range(numvert):
		for v, weight in G[u]:
			edges.append((weight,u,v))

	edges.sort()

	tree = []
	for weight,u,v in edges:
		if disjoint.findset(u) != disjoint.findset(v):
			tree.append((u,v))
			disjoint.union(u,v)

	print(tree)


def main():
    G = []
    file=open('input1.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)
    file.close()

    kruskals(G)

if __name__ == '__main__' :
        main()