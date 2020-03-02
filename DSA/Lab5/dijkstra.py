
# def dijkstra(G,v)
#     dist_so_far = {}
#     dist_so_far[v] = 0
#     final_dist = {}

#     while len(final_dist) < len(G):
#         w = shortest_node(dist_so_far)
#         final_dist[w] = dist_so_far[w]
#         del dist_so_far[w]

#         for x in G[w]:
#             if x not in final_dist:
#                 if x not in dist_so_far:
#                     dist_so_far[x] = final_dist[w] + G[w][x]
#                 elif final_dist[w] + G[w][x] < dist_so_far[x]:
#                     dist_so_far[x] = final_dist[w] + G[w][x]

#     return final_dist
import heapq
def dijkstra(HG, v):
    dist_so_far = {v: 0}
    final_dist = {}
    heap = [(0, v)]
    while dist_so_far:
        (w, k) = heapq.heappop(heap)
        if k in final_dist or (k in dist_so_far and w > dist_so_far[k]):
            continue
        else:
            del dist_so_far[k]
            final_dist[k] = w
        for neighbor in [nb for nb in HG[k] if nb not in final_dist]:
            nw = final_dist[k]+ HG[k][neighbor][1]
            if neighbor not in dist_so_far or nw < dist_so_far[neighbor]:
                dist_so_far[neighbor] = nw
                heapq.heappush(heap, (nw, neighbor))
    return final_dist

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
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
    print(dijkstra(G,0))    

if __name__ == '__main__':
    main()