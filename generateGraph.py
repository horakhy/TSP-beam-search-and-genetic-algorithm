
import matplotlib.pyplot as plt
from graph import cities, distances
import networkx as nx

def generate_graph(cities, distances):
    G = nx.Graph()
    for city in cities:
        G.add_node(city)
    for city1 in distances:
        for city2 in distances[city1]:
            G.add_edge(city1, city2, weight=distances[city1][city2])

    # Draw the graph using Matplotlib
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=100, font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=2)
    plt.savefig('graph.png')

## generate graph from cities and costs (list, list)
def generate_path(path):
    G = nx.Graph()
    for city in path:
        G.add_node(city)
    for i in range(len(path)-1):
        G.add_edge(path[i], path[i+1])

    # Draw the graph using Matplotlib
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=20, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=16)
    plt.savefig('path.png')

generate_graph(cities, distances)
