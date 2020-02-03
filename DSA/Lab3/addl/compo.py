from collections import deque
adj=[]
vis=[0 for i in range(100)]
count=[1]
def bfs(node):
	
	q=deque([node])
	vis[node]=count[0]
	while q:
		print(q[0],end=" ")
		top=q.popleft()
		for i in adj[top]:
			if vis[i]==0:
				q.append(i)
				vis[i]=count[0]

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
		if(vis[i]==0):
			bfs(i)
			count[0]+=1
	print('total no of componenets: ',count[0]-1)
	for i in vis[0:len(adj)]:
		print(i,end=" ")


if __name__ == '__main__':
	main()