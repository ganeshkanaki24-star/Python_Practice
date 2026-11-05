# 35. Detect a cycle in a directed and undirected graph.

# Directed Graph Cycle Detection

directed_graph = {
    0: [1],
    1: [2],
    2: [0],
    3: []
}

visited = set()
path = set()

def directed_cycle(node):

    visited.add(node)
    path.add(node)

    for neighbor in directed_graph[node]:

        if neighbor not in visited:
            if directed_cycle(neighbor):
                return True

        elif neighbor in path:
            return True

    path.remove(node)

    return False


has_cycle = False

for node in directed_graph:

    if node not in visited:

        if directed_cycle(node):
            has_cycle = True
            break

print("Directed graph has cycle:", has_cycle)


# Undirected Graph Cycle Detection

undirected_graph = {
    0: [1],
    1: [0, 2],
    2: [1, 0]
}

visited = set()

def undirected_cycle(node, parent):

    visited.add(node)

    for neighbor in undirected_graph[node]:

        if neighbor not in visited:

            if undirected_cycle(neighbor, node):
                return True

        elif neighbor != parent:
            return True

    return False


has_cycle = False

for node in undirected_graph:

    if node not in visited:

        if undirected_cycle(node, -1):
            has_cycle = True
            break

print("Undirected graph has cycle:", has_cycle)