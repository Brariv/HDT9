import networkx as nx
import matplotlib.pyplot as plt


def txtreader(file):
    read = []
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        for line in lines:
            words = line.split(',')
            words = [word.replace('“', '') for word in words]
            words = [word.replace('”', '') for word in words]
            words = [word.replace(' ', '') for word in words]   
            read.append(words)
    return read

G = nx.Graph()
print(txtreader('rutas.txt'))
rutas = txtreader('rutas.txt')
for ruta in rutas:
    G.add_node(ruta[0])
for ruta in rutas:
    G.add_edge(ruta[0], ruta[1], weight=int(ruta[2]))

options = {
    "font_size": 16,
    "font_color": "grey",
    "node_size": 1500,
    "node_color": "white",
    "edgecolors": "purple",
    "linewidths": 5,
    "width": 4,
}

nx.draw(G, with_labels=True, **options)
plt.show()

def dijkstra(graph, start, end):
    visited = {start: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges(min_node):
            if (min_node, edge) in graph:
                weight = current_weight + graph[min_node][edge]['weight']
            if edge[1] not in visited or weight < visited[edge[1]]:
                visited[edge[1]] = weight
                path[edge[1]] = min_node

        if min_node == end:
            break

    if end not in path:
        return "No se encontro un camino."

    shortest_path = []
    node = end
    while node != start:
        shortest_path.append(node)
        node = path[node]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

print("Ingrese la ciudad de origen: ")
origen = input()
print("Ingrese la ciudad de destino: ")
destino = input()

print(dijkstra(G, origen, destino))

