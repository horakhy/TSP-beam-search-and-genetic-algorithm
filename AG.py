from generateGraph import generate_graph
from graph import cities, distances
import time
import random

## Initialize population (Paths)
## Crossover
## Mutation
## Select survivors

generations = 2
population_size = 10
mutation_rate = 0.1
crossover_rate = 0.7

population = []

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
    print("Initializing population...")

    for _ in range(population_size):
        cities = list(distances)
        random.shuffle(cities)
        
        cities.append(cities[0])

        population.append(Individual(cities, determine_fitness(cities)))
        
    print(population)

## Calcula distância em um indivíduo (Caminho)
def distance(path):
    return sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])

## Aleatório 
def mutation(path):
    return path

## Menor caminho
def determine_fitness(path):
    return distance(path)

## Seleciona os melhores caminhos e faz troca entre eles
def crossover(parent1, parent2):
    size = len(parent1)
    a = random.randint(0, size - 1)
    b = random.randint(0, size - 1)

    if a > b:
        a, b = b, a

    mask = [False] * size

    for i in range(a, b + 1):
        mask[i] = True

    # make sure that the first and last cities are the same in child
    child = [-1] * size
    child[a:b+1] = parent1[a:b+1]
    j = b + 1
    for i in range(size):
        print (i)
        
        if child[j % size] == -1:
            child[j % size] = parent2[i]
            j += 1
        else:
            while child[j % size] != -1:
                j += 1
            child[j % size] = parent2[i]


    print ("Parent 1: ", parent1)
    print ("Parent 2: ", parent2)
    print ("Child: ", child, "\n")
    return child


def genetic_algorithm(generations):
    initialize_population()

    for _ in range(generations):
        for individual in range(len(population) - 1):
            # if random.random() < mutation_rate:
            #     individual.path = mutation(individual.path)
            #     individual.fitness = determine_fitness(individual.path)
            crossover(population[0].path, population[1].path)

genetic_algorithm(generations)