from queue import PriorityQueue
v = int(input("Enter number of vertices: "))
g = [[] for _ in range(v)]
def bfs(s, t, n):
    vis = [False] * n
    q = PriorityQueue()
    q.put((0, s))
    vis[s] = True
    while not q.empty():
        u = q.get()[1]
        print(u, end=" ")
        if u == t:
            break
        for v, c in g[u]:
            if not vis[v]:
                vis[v] = True
                q.put((c, v))
    print()
    
def add_edge(x, y, c):
    g[x].append((y, c))
    g[y].append((x, c))
e = int(input("Enter number of edges: "))
for _ in range(e):
    x, y, c = map(int, input("Enter edge (from to cost): ").split())
    add_edge(x, y, c)
s = int(input("Enter start node: "))
t = int(input("Enter target node: "))
bfs(s, t, v)
