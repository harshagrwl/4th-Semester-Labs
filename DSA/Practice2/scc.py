def fillstack(u,vis,stack,G):
	vis[u] = 1
	for v in G[u]:
		if vis[v] == 0:
			fillstack(v,vis,stack,G)
	stack = stack.append(u)


def reversegraph(G):
	Gr = [[] for x in range(len(G))]
	for u in range(len(G)):
		for v in G[u]:
			Gr[v].append(u)
	return Gr

def dfs(G,s,vis):
	vis[s] = 1
	print(s, end=" ")

	for x in G[s]:
		if vis[x] == 0:
			dfs(G,x,vis)


def scc(G):
	num = len(G)
	stack = []
	vis = [0]*num

	for u in range(num):
		if vis[u] == 0:
			fillstack(u,vis,stack,G)

	Gr = reversegraph(G)

	vis = [0]*num

	while stack:
		i = stack.pop()
		if vis[i] == 0:
			dfs(Gr,i,vis)
			print()

def main():
    
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

    scc(G)    

if __name__ == '__main__':

    main()