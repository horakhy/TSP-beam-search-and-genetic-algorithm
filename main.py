from generateGraph import generate_graph, generate_path
from graph import cities, distances
import random
import time

## "Traveling Salesman Problem solved with beam search algorithm"

def distance(path):
    return sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])

def beam_search(cities, beam_size):
    paths = [[city] for city in cities]
    # print("Paths: ", paths)

    while len(paths[0]) < len(cities):
        candidates = []
        random.shuffle(paths) ## Shuffle paths to search for the 
        for path in paths:
            for city in cities:
                if city not in path:
                    # print("asdasdasd", paths[0][0])
                    candidate = path + [city]
                    candidates.append((distance(candidate), candidate))
                # print("Candidate: ", candidates)
        paths = [candidate for (_, candidate) in sorted(candidates)[:beam_size]]
        #print ("Candidates: ", candidates)
    paths[0].append(paths[0][0])
    # print ("Path: ", paths)

    return paths[0], distance(paths[0])

start_time = time.time()
found_path, found_total_distance = beam_search(cities, 50)
end_time = time.time()

print ("Found path: ", found_path)
print ("Found total distance: ", found_total_distance)
print (f"Time taken: {end_time - start_time} s", )

generate_graph(cities, distances)
# generate_path(found_path, found_total_distance)





