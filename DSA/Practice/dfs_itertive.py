from collections import deque
adj=[]
vis=[0 for i in range(6)]
start=[-1 for i in range(6)]
finish=[-1 for i in range(6)]
time = 0

def dfs(node):
	s = deque()
	s.append(node)
	while s:
		t = s.pop()
		if vis[t] == 0:
			print(t,end=" ")
			vis[t] = 1
		for i in reversed(adj[t]):
			if vis[i] == 0:
				s.append(i)

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
	
	file.close()
	
	dfs(0)
	print("Start time: ",start,end=" ")
	print("Finish time: ",finish,end=" ")

if __name__ == '__main__':
	main()