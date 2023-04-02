from beam import beam_search
from graph import generate_adjacent_list, cities
import matplotlib.pyplot as plt
import numpy as np

beam_size = 5
generations = 10
distances = generate_adjacent_list()
distances_data_to_plot = []
beam_size_data_to_plot = []

for i in range(1, 11):
    print("Beam Size: ", beam_size * i)
    _, distance_found = beam_search(cities, distances, beam_size * i)
    distances_data_to_plot.append(distance_found)
    beam_size_data_to_plot.append(beam_size * i)
print ()
print("Distances: ", distances_data_to_plot)
print("Beam Size: ", beam_size_data_to_plot)

plt.title('Local beam algorithm')
plt.ylabel('Distance')
plt.xlabel('Generation')
plt.plot(beam_size_data_to_plot, distances_data_to_plot)
plt.savefig('Beam_results.png')


