v = int(input("Enter number of vertices: "))
g = [[] for _ in range(v)]
def dfs(s, n):
    vis = [False] * n
    stack = [s]
    vis[s] = True
    while stack:
        u = stack.pop()
        print(u, end=" ")
        for v in g[u]:
            if not vis[v]:
                vis[v] = True
                stack.append(v)
    print()
    
def add_edge(x, y):
    g[x].append(y)
    g[y].append(x)
    
e = int(input("Enter number of edges: "))
for _ in range(e):
    x, y = map(int, input("Enter edge (from to): ").split())
    add_edge(x, y)
s = int(input("Enter start node: "))
dfs(s, v)
