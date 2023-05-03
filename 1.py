from collections import defaultdict

# function to add an edge to the graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# function for DFS traversal
def dfs(graph, source, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(source)
    if source == goal:
        return [source]
    for neighbor in graph[source]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if path:
                return [source] + path
    return None

# function for BFS traversal
def bfs(graph, source, goal):
    visited = set()
    queue = [[source]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# create the graph
graph = defaultdict(list)
n = int(input("Enter the number of edges: "))
for i in range(n):
    u, v = input("Enter edge (u, v): ").split()
    add_edge(graph, u, v)

# get the source and goal nodes from the user
source = input("Enter the source node: ")
goal = input("Enter the goal node: ")

# perform DFS traversal
print("DFS traversal:", dfs(graph, source, goal))

# perform BFS traversal
print("BFS traversal:", bfs(graph, source, goal))
