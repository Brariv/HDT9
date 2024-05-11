
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
            read.append(words)
    return read

G = nx.Graph()
rutas = txtreader('rutas.txt')

##G.add_nodes_from(rutas[0][0], rutas[0][1], rutas[0][2], rutas[0][3])
for ruta in rutas:
    G.add_edge(ruta[0], ruta[1], weight=int(ruta[2]))

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw(G, with_labels=True, **options)
plt.show()



def dijkstra(graph, start):
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
            weight = current_weight + graph[min_node][edge]['weight']
            if edge[1] not in visited or weight < visited[edge[1]]:
                visited[edge[1]] = weight
                path[edge[1]] = min_node

    return visited, path


print(txtreader('rutas.txt'))