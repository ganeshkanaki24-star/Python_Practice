# 36. Implement topological sorting for a directed acyclic graph.

graph = {
    0: [2, 3],
    1: [3, 4],
    2: [5],
    3: [5],
    4: [5],
    5: []
}

visited = set()
stack = []

def topological_sort(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            topological_sort(neighbor)

    stack.append(node)


for node in graph:

    if node not in visited:
        topological_sort(node)

stack.reverse()

print("Topological Order:", stack)