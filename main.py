from generateGraph import generate_graph
from graph import cities, distances
import time

## "Traveling Salesman Problem solved with beam search algorithm"

def distance(path):
    return sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])

def beam_search(cities, beam_size=10):
    paths = [[city] for city in cities]
    print("Paths: ", paths)
    while len(paths[0]) < len(cities):
        candidates = []
        for path in paths:
            for city in cities:
                if city not in path:
                    candidate = path + [city]
                    candidates.append((distance(candidate), candidate))
        paths = [candidate for (_, candidate) in sorted(candidates)[:beam_size]]
    return paths[0], distance(paths[0])

start_time = time.time()
found_path, found_total_distance = beam_search(cities, 3)
end_time = time.time()

print ("Found path: ", found_path)
print ("Found total distance: ", found_total_distance)
print (f"Time taken: {end_time - start_time} s ", )

generate_graph(cities, distances)





