from generateGraph import generate_graph
from graph import cities, distances
import time
import random

## Initialize population (Paths)
## Crossover
## Mutation
## Select survivors

generations = 50
population_size = 50
mutation_rate = 0.1
crossover_rate = 0.9

population = []
## initialize biggest int

mean_fitnes = 0

class Individual:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness

    def __repr__(self):
        return f"Individual({self.path}, {self.fitness})\n"

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

def initialize_population():
    #print("Initializing population...")
    global population
    population = []

    for _ in range(population_size):
        cities = list(distances)
        random.shuffle(cities)
        
        cities.append(cities[0])
        
        population.append(Individual(cities, determine_fitness(cities)))
        
    return population

## Calcula distância em um indivíduo (Caminho)
def distance(path):
    return sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])

## Aleatório 
def mutation(path):
    
    idx1, idx2 = random.sample(range(len(cities)), 2)
    # print (idx1,idx2)
    path[idx1], path[idx2] = path[idx2], path[idx1]
    
    return path

## Menor caminho
def determine_fitness(path):
    return 1 / distance(path)

## Seleciona os melhores caminhos e faz troca entre eles
def crossover(parent1, parent2):
    n = len(parent1)
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    if a > b:
        a, b = b, a
    
    # Copy subset of parent1 into offspring
    offspring = [-1] * n
    offspring[a:b+1] = parent1[a:b+1]

    # print("Offspring First: ", offspring)
    # print()
    
    # Add remaining genes from parent2
    index = b+1
    for i in range(n):
        if index == n:
            index = 0
        if parent2[i] not in offspring:
            offspring[index] = parent2[i]
            index += 1
        # print("Offspring in process: ", offspring)
        # print()
    if(-1 in offspring):
        offspring[offspring.index(-1)] =  offspring[-1] if offspring[-1] != -1 else offspring[0]
    offspring[-1] = offspring[0]
    
    # print("Parent 1: ", parent1)
    # print("Parent 2: ", parent2)
    # print("Offspring: ", offspring)

    return offspring

def update_population():
    global population
    population.sort(key=lambda individual: individual.fitness, reverse=True)
    population = population[:population_size]

def genetic_algorithm(generations):
    initial_population = initialize_population()
    initial_population.sort(key=lambda individual: individual.fitness, reverse=True)
    
    for _ in range(generations):
        for index in range(len(population)):
            if index == 0:
                continue
            # if random.random() < mutation_rate:
            #     individual.path = mutation(individual.path)
            #     individual.fitness = determine_fitness(individual.path)
            
            if random.random() * population[index].fitness < crossover_rate:
                offspring = crossover(population[index - 1].path, population[index].path)
                population.append(Individual(offspring, determine_fitness(offspring)))
            
            if random.random() < mutation_rate and distance(population[index].path) > distance:
                population[index].path = mutation(population[index].path)
                population[index].fitness = determine_fitness(population[index].path)

            update_population()
            
            # print("Fitness do melhor: ", population[0].fitness)
    
    print("Distancia do melhor: ", distance(population[0].path))
    print("Distancia População inicial: ", distance(initial_population[0].path))
    return distance(population[0].path)

mean_dist = 0

for i in range(100):
    print("Execução: ", i)
    mean_dist += genetic_algorithm(generations)

print("Distancia média: ", mean_dist/100) 

