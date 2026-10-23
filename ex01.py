import heapq
graph = {}
def UCS(start,goal):
    pq = [(0,start,[start])] # cost,node,path
    visited = set()
    while pq:
        cost,node,path = heapq.heappop(pq)
        if node in visited:
            continue
        if node==goal:
            return path,cost
        for nei,edge_cost in graph[node]:
            if nei not in visited:
                heapq.heappush(pq,(cost+edge_cost,nei,path+[nei]))
    return None,float('inf')

def dls(current,goal,limit,visited,path):
    visited.add(current)
    path.append(current)
    if current == goal:
        return True
    if limit==0:
        path.pop()
        return False

    for nei in graph[current]:
        if nei not in visited:
            if dls(nei,goal,limit-1,visited,path):
                return True
    path.pop()
    return False

def iddfs(start,goal,max_depth=1):
    for limit in range(1,max_depth+1,3):
        visited = set()
        path = []
        if dls(start,goal,limit,visited,path):
            print("found")
            print("path:", "->".join(path))
            return
        
        print("not found")


def dfs(node,goal,visited,path):
    visited.add(node)
    path.append(node)
    if node==goal:
        return True
    
    for nei in graph[node]:
        if nei not in visited:
            if dfs(nei,goal,visited,path):
                return True
    path.pop()
    return False
