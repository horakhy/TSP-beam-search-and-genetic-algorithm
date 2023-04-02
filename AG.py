from generateGraph import generate_graph
from graph import cities, generate_adjacent_list
import time
import random

## Initialize population (Paths)
## Crossover
## Mutation
## Select survivors

generations = 500
population_size = 200
mutation_rate = 0.01
crossover_rate = 0.85
reproduction_quocient = int(0.75 * population_size)

population = []
## initialize biggest int

mean_fitnes = 0
distances = generate_adjacent_list()

class Individual:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness

    def __repr__(self):
        return f"Individual({self.path}, {self.fitness})\n"

def initialize_population():
    global population
    population = []

    for _ in range(population_size):
        path = list(distances)
        random.shuffle(path)
        
        path.append(path[0])
        
        population.append(Individual(path, determine_fitness(path)))
        
    return population

## Calcula distância em um indivíduo (Caminho)
def distance(path):
    return sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])

## Aleatório troca posição de um gene/cidade
def mutation(path):
    
    idx1, idx2 = random.sample(range(len(cities) - 2), 2)

    path[idx1], path[idx2] = path[idx2], path[idx1]

    return path

## Menor caminho
def determine_fitness(path):
    return 1 / distance(path)

## Retorna dois filhos que são combinações aleatórias dos pais
def crossover(parent1, parent2):
    point_1, point_2 = random.sample(range(0, len(parent1)-1), 2)
    begin = min(point_1, point_2)
    end = max(point_1, point_2)

    offspring_1 = parent1[begin:end+1]
    offspring_2 = parent2[begin:end+1]

    offspring_1_remain = [item for item in parent2[0:-1] if item not in offspring_1]
    offspring_2_remain = [item for item in parent1[0:-1] if item not in offspring_2]

    offspring_1 += offspring_1_remain
    offspring_2 += offspring_2_remain

    offspring_1.append(offspring_1[0])

    offspring_2.append(offspring_2[0])

    return offspring_1, offspring_2

def update_population():
    global population
    population.sort(key=lambda individual: individual.fitness, reverse=True)
    population = population[:population_size]

def genetic_algorithm(generations, distances_test):
    global distances
    distances = distances_test

    initial_population = initialize_population()
    initial_population.sort(key=lambda individual: individual.fitness, reverse=True)
    
    for _ in range(generations):
       
        for index in range(len(population)):
            if index == 0:
                continue
            
            ## Only 75% of the population can reproduce and mutate
            # if index == reproduction_quocient:
            #     break;
            
            if random.random() < crossover_rate:
                offspring_1, offspring_2 = crossover(population[index - 1].path, population[index].path)
                population.append(Individual(offspring_1, determine_fitness(offspring_1)))
                population.append(Individual(offspring_2, determine_fitness(offspring_2)))
            
            if random.random() < mutation_rate:
                population[index].path = mutation(population[index].path)
                population[index].fitness = determine_fitness(population[index].path)

            update_population()
            
            # print("Fitness do melhor: ", population[0].fitness)
    
    print("Melhor: ", population[0].path)
    print("Distancia do melhor: ", distance(population[0].path))
    print("Distancia População inicial: ", distance(initial_population[0].path))
    print()
    return distance(population[0].path)

# mean_dist = 0

# for i in range(10):
#     print("Execução: ", i)
#     start_time = time.time()
#     mean_dist += genetic_algorithm(generations)
#     end_time = time.time()
#     mean_time = (end_time - start_time)

# print("Distancia média: ", mean_dist/10) 
# print("Tempo médio de execução: ", mean_time/10)

