from AG import genetic_algorithm
from graph import generate_adjacent_list
import matplotlib.pyplot as plt
import numpy as np

generations = 50
distances = generate_adjacent_list()
distances_data_to_plot = []
generations_data_to_plot = []

for i in range(1, 16):
    print("Generation Size: ", generations * i)
    distances_data_to_plot.append(genetic_algorithm(generations * i, distances))
    generations_data_to_plot.append(generations * i)
print ()
print("Distances: ", distances_data_to_plot)
print("Generations: ", generations_data_to_plot)

plt.title('Genetic Algorithm')
plt.ylabel('Distance')
plt.xlabel('Generation')
plt.plot(generations_data_to_plot, distances_data_to_plot)
plt.savefig('AG_results_2.png')



