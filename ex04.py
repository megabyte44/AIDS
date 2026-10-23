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
