variables = ['A', 'B', 'C', 'D']
domains = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C','D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C','A']
}

assignment = {}

def isok(var,color):
    for nei in graph[var]:
        if assignment.get(nei)==color:
            return False
    return True

def backtrack():
    if len(assignment)==len(variables):
        return True
    
    var = next(v for v in variables if v not in assignment)

    for color in domains:
        if isok(var,color):
            assignment[var]=color
            if backtrack():
                return True
            del assignment[var]
    return False
    