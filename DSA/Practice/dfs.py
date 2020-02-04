adj=[]
vis=[0 for i in range(6)]
start=[-1 for i in range(6)]
finish=[-1 for i in range(6)]
time = 0

def dfs(node):
	global time
	vis[node] = 1
	print(node,end=" ")
	start[node] = time
	time +=1
	for i in adj[node]:
		if vis[i] == 0:
			dfs(i)
	finish[node] = time
	time+=1

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
			dfs(i)
	file.close()
	print("Start time: ",start,end=" ")
	print("Finish time: ",finish,end=" ")

if __name__ == '__main__':
	main()