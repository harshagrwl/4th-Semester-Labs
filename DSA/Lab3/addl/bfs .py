from collections import deque
adj=[]
vis=[0 for i in range(1000)]

def bfs(node):
	q=deque([node])
	vis[node]=1
	while q:
		node=q.popleft()
		print(node,end=" ")
		for i in adj[node]:
			if vis[i]==0:
				q.append(i)
				vis[i]=1

def main():
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		temp=[]
		flg=1
		for node in line.split():
			if flg==1:
				flg=0
				continue
			temp.append(int(node))
		adj.append(temp)

	for i in range(0,len(adj)):
		if vis[i]==0:
			bfs(i)

if __name__ == '__main__':
	main()