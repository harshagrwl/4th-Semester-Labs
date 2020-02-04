from collections import deque
adj=[]
start=[-1 for i in range(6)]
vis=[0 for i in range(6)]
finish = [-1 for i in range(6)]
time = 0
pred = [-1 for i in range(6)]
ap = [0 for i in range(6)]


def twoegde(u):
        global time
        global vis,finish,start,adj,pred,ap
        child = 0
        vis[u] = 1
        start[u] = time
        time += 1
        sst = start[u]
        for i in adj[u]:
                if vis[i] == 0:
                        pred[i] = u
                        child += 1
                        sst = min(twoegde(i),sst)
                else:
                        if pred[u] != i and start[u] > start[i]:
                                sst = min(start[i],sst)
        finish[u] = time
        time += 1
        if u==0 and child > 1:
                ap[u] = 1
        if sst == start[u] and u!=0:
                ap[u] = 1
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

        for i in range(len(adj)):
                if vis[i] == 0:
                        twoegde(i)
        for index, value in enumerate (ap): 
                if value == 1: print(index, end=" ")


if __name__ == '__main__':
        main()