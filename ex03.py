# Experiment 3: Implement Genetic Algorithms for AI Tasks (8-Queens Problem)
import random

N = 8
POP_SIZE = 100
MAX_GEN = 1000
MUTATION_RATE = 0.03

def create_chromosome():
    return random.sample(range(N),N)

def fitness(ch):
    max_pairs = N*(N-1)//2

    attacks = 0

    for i in range(N):
        for j in range(i+1,N):
            if ch[i]==ch[j] or abs(ch[i]-ch[j])==j-i:
                attacks+=1
    return (max_pairs-attacks)/max_pairs
def print_board(ch):
    for i in range(N):
        for j in range(N):
            if ch[j] == i:
                print("Q",end=" ")
            else:
                print(".",end =" ")
        print()
def selection(population):
    fitness_v = [fitness(ch) for ch in population]
    total =  sum(fitness_v)
    if total == 0 :
        return random.choice(population)
    return random.choices(population,weights = fitness_v,k=1)[0]
def crossover(p1,p2):
    point = random.randint(1,N-2)
    return p1[:point] + p2[point:]
def mutation(ch):
    if random.random() < MUTATION_RATE:
        i = random.randrange(N)
        ch[i] = random.randrange(N)
    return ch
def genetic_algo():
    population = [create_chromosome() for _ in range(POP_SIZE)]

    for generation in range(MAX_GEN):
        population.sort(key=fitness,reverse = True)
        best = population[0]
        print("best Solution",best)
        print("Fitness",fitness(best))
        print_board(best)

        if fitness(best)== 1.0:
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
            child = mutation(crossover(p1,p2))
            new_population.append(child)
        population = new_population
    
    best = max(population,key = fitness)
    print("best Solution",best)
    print("Fitness",fitness(best))
    print_board(best)

genetic_algo()

