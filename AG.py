from generateGraph import generate_graph
from graph import cities, distances
import time

## Initialize population (Paths)
## Crossover
## Mutation
## Select survivors

generations = 10
population_size = 10
mutation_rate = 0.1
crossover_rate = 0.7

population = []

class Individual:
    def __init__(self, identifier, path):
        self.identifier = identifier
        self.path = path
        self.fitness = 0

    def __repr__(self):
        return f"Individual({self.identifier}, {self.path}, {self.fitness})\n"

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

def initialize_population():
    print("Initializing population...")

    for key, value in distances.items():
        population.append(Individual(key, value))
        
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
def crossover(path1, path2):
    return path1, path2


def genetic_algorithm(generations, population_size, mutation_rate, crossover_rate):
    for _ in generations:
        # Crossover

        # Mutation
        # Select survivors
        pass

initialize_population()