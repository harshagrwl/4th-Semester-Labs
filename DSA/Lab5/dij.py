import sys
import heapq
class graph:
        def __init__(self,G):
         
            self.list=G
            self.visited=[0 for i in range(len(self.list))]
            self.ls=[]
            self.v=len(self.list)
            self.pred=None
            self.dis=[]
            self.ans={}

            

        def dijkistra(self,s):
            for i in range(self.v):
                self.dis.append(100)
            self.dis[s]=0
            self.ans[s]=0
            for i in range(self.v):
            	#self.ls[i]=self.dis[i]
                self.ls.append([self.dis[i],i])

            heapq.heapify(self.ls)
            print(self.ls)

            while(True):
                ls=heapq.heappop(self.ls)
                #ls=self.ls[0]
                u=ls[1]
                print(u)
                if(ls[0]==100):
                	break
                ls=self.list[u]
                for edge in ls:
                    v=edge[0]
                    w=edge[1]
                    if self.dis[v]>self.dis[u]+w:
                        self.dis[v]=self.dis[u]+w
                        lt=[self.dis[v],v]
                        self.ans[v]=self.dis[v]
                        self.ls.append(lt)
                        heapq.heapify(self.ls)
            for key,values in self.ans.items():
            	print(key,values,sep=" ")
                        








def main():
    ''' Adjacency List representation. G is a list of lists. '''
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

    print(G)
    g=graph(G)
    g.dijkistra(1)

if __name__ == '__main__':
    main()

