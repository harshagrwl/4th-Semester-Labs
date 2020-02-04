from collections import deque
adj=[]
start=[-1 for i in range(6)]
vis=[0 for i in range(6)]
finish = [-1 for i in range(6)]
time = 0
pred = [0 for i in range(6)]

def twoegde(u):
	global time
	global vis,finish,start,adj,pred
	vis[u] = 1
	start[u] = time
	time += 1
	sst = start[u]
	for i in adj[u]:
		if vis[i] == 0:
			pred[i] = u
			sst = min(twoegde(i),sst)
		else:
			if pred[u] != i and start[u] > start[i]:
				sst = min(start[i],sst)
	finish[u] = time
	time += 1
	if sst == start[u] and u!=0:
		print(f"exit at {u} and Not 2 edge connected")
		exit()
	return sst


def main():
	file=open('input.txt','r')
	for line in file:
		line=line.strip()
		temp=[]
		flag=1
		for node in line.split():
			if flag==1:
				flag=0
				continue
			temp.append(int(node))
		adj.append(temp)

	twoegde(0)
	print("Two edge connected")


if __name__ == '__main__':
	main()