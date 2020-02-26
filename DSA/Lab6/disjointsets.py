class Node:
    def __init__(self,x):
        self.val = x
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.val)


def makeset(x):
    x.parent = x
    x.rank   = 0

def union(x, y):
    xRoot = findset(x)
    yRoot = findset(y)
    if xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    elif xRoot.rank < yRoot.rank:
        xRoot.parent = yRoot
    elif xRoot != yRoot: # Unless x and y are already in same set, merge them
        yRoot.parent = xRoot
        xRoot.rank = xRoot.rank + 1

def findset(x):
    if x.parent!=x:
        x.parent = findset(x.parent)
    return x.parent
   
def main():
    #ds = DisjointSets()
    #nodes = [Node(i) for i in range(10)]

    # [makeset(node) for node in nodes]
    # print("It Works")
    # union(nodes[0],nodes[1])
    # print(findset(nodes[0]))    # Should print 1
    # union(nodes[0],nodes[2])
    # print(findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''
    nodes = [Node(i) for i in [0,1,2,3]]
    makeset(nodes[0])
    makeset(nodes[1])
    makeset(nodes[2])
    makeset(nodes[3])
    union(nodes[0], nodes[1])
    union(nodes[1], nodes[2])
    union(nodes[2], nodes[3])
    print(findset(nodes[3]))
    print(findset(nodes[2]))
    print(findset(nodes[1]))
    print(findset(nodes[0]))

if __name__ == '__main__':
    main()
