# CSE325: AI & DATA SCIENCE LABORATORY
## PART 1: EXPERIMENTS 1 TO 6 (ARTIFICIAL INTELLIGENCE)

---

# Experiment 1: Implement Basic Search Strategies for Selected AI Applications

### 1(A) Breadth-First Search (BFS)
```python
from collections import deque

# -----------------------------
# Graph Representation
# -----------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': ['K'],
    'I': [],
    'J': [],
    'K': []
}

# -----------------------------
# Breadth First Search
# -----------------------------
def bfs(start, goal):
    # Queue (FIFO)
    queue = deque()

    # Store path
    queue.append((start, [start]))

    # Visited Nodes
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        # Goal Test
        if current == goal:
            return path

        # Visit Neighbours
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None

# -----------------------------
# Driver Code
# -----------------------------
start = 'A'
goal = 'K'

path = bfs(start, goal)

if path:
    print("Path Found:")
    print(" -> ".join(path))
else:
    print("No Path Found")
```

---

### 1(B) Depth-First Search (DFS)
```python
# -----------------------------
# Graph Representation
# -----------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': ['K'],
    'I': [],
    'J': [],
    'K': []
}

# -----------------------------
# Depth First Search
# -----------------------------
def dfs(current, goal, visited, path):
    # Mark current node as visited
    visited.add(current)

    # Add current node to path
    path.append(current)

    # Goal Test
    if current == goal:
        return True

    # Visit all neighbours
    for neighbour in graph[current]:
        if neighbour not in visited:
            if dfs(neighbour, goal, visited, path):
                return True

    # Backtrack
    path.pop()
    return False

# -----------------------------
# Driver Code
# -----------------------------
start = 'A'
goal = 'K'

visited = set()
path = []

if dfs(start, goal, visited, path):
    print("Path Found:")
    print(" -> ".join(path))
else:
    print("No Path Found")
```

---

### 1(C) Uniform Cost Search (UCS)
```python
import heapq

graph = {
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagaras', 99)],
    'Rimnicu Vilcea': [('Pitesti', 97)],
    'Fagaras': [('Bucharest', 211)],
    'Pitesti': [('Bucharest', 101)],
    'Bucharest': []
}

def ucs(start, goal):
    priority_queue = [(0, start, [start])]  # (cost, current node, path)
    visited = set()

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, cost

        for neighbour, edge_cost in graph[current]:
            if neighbour not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbour, path + [neighbour]))

    return None, float('inf')

# Driver Code
start, goal = "Sibiu", "Bucharest"
path, total_cost = ucs(start, goal)

if path:
    print("Path Found:")
    print(" -> ".join(path))
    print("Total Cost:", total_cost)
else:
    print("No Path Found")
```

---

### 1(D) Depth-Limited Search (DLS)
```python
# Graph Representation
graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': ['G', 'H'], 'E': [], 'F': ['I', 'J'],
    'G': [], 'H': [], 'I': [], 'J': []
}

# Depth Limited Search
def dls(current, goal, limit, visited, path):
    visited.add(current)
    path.append(current)

    if current == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbour in graph[current]:
        if neighbour not in visited:
            if dls(neighbour, goal, limit - 1, visited, path):
                return True

    path.pop()
    return False

# Driver Code
start, goal, depth_limit = 'A', 'H', 3
visited, path = set(), []

if dls(start, goal, depth_limit, visited, path):
    print("Goal Found")
    print("Path :", " -> ".join(path))
else:
    print("Goal Not Found within Depth Limit")
```

---

### 1(E) Iterative Deepening Depth-First Search (IDDFS)
```python
# Graph Representation
graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': ['G', 'H'], 'E': [], 'F': ['I', 'J'],
    'G': [], 'H': [], 'I': [], 'J': []
}

# Depth Limited Search
def dls(current, goal, limit, visited, path):
    visited.add(current)
    path.append(current)

    if current == goal:
        return True
    if limit == 0:
        path.pop()
        return False

    for neighbour in graph[current]:
        if neighbour not in visited:
            if dls(neighbour, goal, limit - 1, visited, path):
                return True

    path.pop()
    return False

# Iterative Deepening DFS
def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Searching at Depth :", depth)
        visited, path = set(), []
        if dls(start, goal, depth, visited, path):
            print("\nGoal Found")
            print("Depth :", depth)
            print("Path :", " -> ".join(path))
            return
    print("\nGoal Not Found")

# Driver Code
iddfs('A', 'H', 5)
```

---

# Experiment 2: Implement A* and Memory Bounded A* Algorithms

### 2(A) A* Algorithm
```python
import heapq

# Graph
graph = {
    'A': [('B', 1), ('C', 4)], 'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)], 'D': [('G', 5)], 'E': [('G', 1)],
    'F': [('G', 2)], 'G': []
}

# Heuristic Values
heuristic = {'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 2, 'F': 1, 'G': 0}

# A* Algorithm
def astar(start, goal):
    frontier = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    explored = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)
        if current == goal:
            return path, g
        explored.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in explored:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Driver Code
path, cost = astar('A', 'G')
if path:
    print("Shortest Path :", " -> ".join(path))
    print("Total Cost :", cost)
else:
    print("No Path Found")
```

---

### 2(B) Memory Bounded A* (IDA*) Algorithm
```python
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 2, 'F': 1, 'G': 0}

def search(node, goal, g, limit, path):
    f = g + h[node]

    if f > limit:
        return None, f

    if node == goal:
        return path, float('inf')

    next_limit = float('inf')

    for neighbor, cost in graph[node]:
        if neighbor not in path:
            result, exceeded = search(neighbor, goal, g + cost, limit, path + [neighbor])

            if result:
                return result, exceeded

            next_limit = min(next_limit, exceeded)

    return None, next_limit

def ida_star(start, goal):
    limit = h[start]

    while True:
        path, next_limit = search(start, goal, 0, limit, [start])

        if path:
            return path

        if next_limit == float('inf'):
            return None

        limit = next_limit

# Driver Code
path = ida_star('A', 'G')
print("Path Found:", " -> ".join(path) if path else "No Path Found")
```

---

# Experiment 3: Implement Genetic Algorithms for AI Tasks (8-Queens Problem)

```python
import random

N = 8
POP_SIZE = 100
MAX_GEN = 1000
MUTATION_RATE = 0.03

def create_chromosome():
    return random.sample(range(N), N) # Create list of 8 randomly placed int (0 to 7)

def fitness(ch):
    max_pairs = N * (N - 1) // 2
    attacks = 0

    for i in range(N):
        for j in range(i + 1, N):
            if ch[i] == ch[j] or abs(ch[i] - ch[j]) == abs(i - j):
                attacks += 1

    return (max_pairs - attacks) / max_pairs

def selection(population):
    fitness_values = [fitness(ch) for ch in population]
    total = sum(fitness_values)

    if total == 0:
        return random.choice(population)

    probabilities = [f / total for f in fitness_values]
    return random.choices(population, weights=probabilities, k=1)[0]

def crossover(p1, p2):
    point = random.randint(1, N - 2)
    return p1[:point] + p2[point:]

def mutate(ch):
    if random.random() < MUTATION_RATE:
        i = random.randrange(N)
        ch[i] = random.randrange(N)
    return ch

def print_board(ch):
    for row in range(N):
        for col in range(N):
            if ch[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def genetic_algorithm():
    population = [create_chromosome() for _ in range(POP_SIZE)]

    for generation in range(MAX_GEN):
        population.sort(key=fitness, reverse=True)
        best = population[0]

        if fitness(best) == 1.0:
            print("Solution Found!")
            print("Generation:", generation)
            print("Queen Placement:", best)
            print("Fitness:", fitness(best))
            print_board(best)
            return

        new_population = []

        while len(new_population) < POP_SIZE:
            p1 = selection(population)
            p2 = selection(population)
            child = mutate(crossover(p1, p2))
            new_population.append(child)

        population = new_population

    best = max(population, key=fitness)
    print("Best Solution:", best)
    print("Fitness:", fitness(best))
    print_board(best)

# Driver Code
genetic_algorithm()
```

---

# Experiment 4: Implement Simulated Annealing Algorithms for AI Tasks (Sudoku Solver)

```python
import random
import math
import copy

board = [
    [5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def initialize(board):
    sudoku = copy.deepcopy(board)
    for i in range(9):
        missing = []
        for num in range(1, 10):
            if num not in sudoku[i]:
                missing.append(num)
        random.shuffle(missing)
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = missing.pop()
    return sudoku

def cost(board):
    conflicts = 0
    for col in range(9):
        values = []
        for row in range(9):
            values.append(board[row][col])
        conflicts += 9 - len(set(values))

    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            values = []
            for i in range(3):
                for j in range(3):
                    values.append(board[br+i][bc+j])
            conflicts += 9 - len(set(values))
    return conflicts

def neighbor(board, fixed):
    sudoku = copy.deepcopy(board)
    row = random.randint(0, 8)
    mutable = []
    for col in range(9):
        if not fixed[row][col]:
            mutable.append(col)
    if len(mutable) >= 2:
        c1, c2 = random.sample(mutable, 2)
        sudoku[row][c1], sudoku[row][c2] = sudoku[row][c2], sudoku[row][c1]
    return sudoku

def simulated_annealing():
    temperature, cooling_rate, stop_temperature = 1000, 0.995, 0.1
    fixed = []
    for row in board:
        temp = []
        for cell in row:
            temp.append(cell != 0)
        fixed.append(temp)

    current = initialize(board)
    current_cost = cost(current)
    best = copy.deepcopy(current)
    best_cost = current_cost

    while temperature > stop_temperature:
        new = neighbor(current, fixed)
        new_cost = cost(new)
        delta = current_cost - new_cost

        if delta > 0:
            current, current_cost = new, new_cost
        else:
            probability = math.exp(delta / temperature)
            if random.random() < probability:
                current, current_cost = new, new_cost

        if current_cost < best_cost:
            best, best_cost = copy.deepcopy(current), current_cost
        if best_cost == 0:
            break
        temperature *= cooling_rate

    return best, best_cost

# Driver Code
solution, conflicts = simulated_annealing()
print("\nBest Sudoku:\n")
for row in solution:
    print(row)
print("\nConflicts =", conflicts)
```

---

# Experiment 5: Implement Alpha-Beta Tree Search

```python
import math

values = []
max_depth = 0

def alpha_beta(depth, node_index, alpha, beta):
    if depth == max_depth:
        return values[node_index]

    if depth % 2 == 0:  # MAX level
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:  # MIN level
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best

# Driver Code
max_depth = int(input("Enter depth of tree: "))

for i in range(2 ** max_depth):
    values.append(int(input(f"Leaf {i + 1}: ")))

result = alpha_beta(0, 0, -math.inf, math.inf)
print("Optimal Value =", result)
```

---

# Experiment 6: Implement Backtracking Algorithms for CSP (Map Coloring)

```python
variables = ['A', 'B', 'C', 'D']
domains = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_consistent(var, color):
    for neighbor in graph[var]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack():
    if len(assignment) == len(variables):
        return True

    var = next(v for v in variables if v not in assignment)

    for color in domains:
        if is_consistent(var, color):
            assignment[var] = color

            if backtrack():
                return True

            del assignment[var]

    return False

# Driver Code
if backtrack():
    print("Map coloring solution:")
    print(assignment)
else:
    print("No solution exists")
```
