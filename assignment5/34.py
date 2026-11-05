# 34. Find the shortest path in a weighted graph using Dijkstra's algorithm.

import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

start = 'A'

distances = {node: float('inf') for node in graph}

distances[start] = 0

priority_queue = [(0, start)]

while priority_queue:

    distance, node = heapq.heappop(priority_queue)

    if distance > distances[node]:
        continue

    for neighbor, weight in graph[node]:

        new_distance = distance + weight

        if new_distance < distances[neighbor]:

            distances[neighbor] = new_distance

            heapq.heappush(priority_queue, (new_distance, neighbor))

print("Shortest distances:", distances)