from collections import deque
def bfs(graph, start):
  visited = set()
  queue = deque([start])

  while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
# Sample graph (Adjacency List)
graph = {
'A': ['B', 'C', 'P'],
'P': ['X', 'Y'],
'X': [],
'Y': [],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': []
}
# Run BFS
print("BFS Traversal starting from node A:")
bfs(graph, 'A')