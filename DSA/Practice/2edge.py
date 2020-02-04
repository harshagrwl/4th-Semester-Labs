def twoEdge(u):
    global time
    global adList, startTime, finishTime, pred, visited, treeEdges
    startTime[u] = time
    time += 1 
    visited[u] = True
    sst = startTime[u]
    for v in adList[u]:
        if not visited[v]:
            treeEdges.append((u,v))
            pred[v] = u
            sst = min(twoEdge(v), sst)
        else:
            if pred[u] != v and startTime[u] > startTime[v]:
                sst = min(startTime[v], sst)
    finishTime[u] = time
    time += 1
    if u != source and sst == startTime[u]:
        print(f"exit at {u} and not edge connected")
        exit()
    return sst