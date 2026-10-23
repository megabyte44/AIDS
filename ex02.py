import heapq

# Graph
graph = {
    'A': [('B', 1), ('C', 4)], 'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)], 'D': [('G', 5)], 'E': [('G', 1)],
    'F': [('G', 2)], 'G': []
}

# Heuristic Values
heuristic = {'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 2, 'F': 1, 'G': 0}

def A_star(start,goal):
    frontier = [(heuristic[start],0,start,[start])]
    explored = set()

    while frontier:
        f,g,node,path = heapq.heappop(frontier)
        if node==goal:
            return path,g
        explored.add(node)

        for nei,cost in graph[node]:
            if nei not in explored:
                heapq.heappush(frontier,(cost+g+heuristic[nei],g+cost,nei,path+[nei]))
        
    return None,float('inf')


def search(node,goal,g,limit,path):
    f = g + heuristic[node]
    if f>limit:
        return None,f
    if node==goal:
        return path,float('inf')
    
    next_limit = float('inf')

    for nei,cost in graph[node]:
        if nei not in path:
            result,exceeded = search(nei,goal,g+cost,limit,path+[nei])
            if result:
                return result,exceeded
            next_limit = min(exceeded,next_limit)
    return None,next_limit
def ida_star(start,goal):
    limit = heuristic[start]
    
    while True:
        path,next_limit = search(start,goal,0,limit,[start])
        if path:
            return path
        if next_limit == float('inf'):
            return None
        limit = next_limit

path = ida_star('A',"G")
print()