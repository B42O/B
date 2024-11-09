from heapq import heappush, heappop

def a(g, h, s, t):
    b = [(h[s], s)]
    c = {s: 0}
    d = {}
    
    while b:
        _, n = heappop(b)
        if n == t:
            e, f = [], c[t]
            while n:
                e.append(n)
                n = d.get(n)
            return e[::-1], f
        
        for i, j in g.get(n, {}).items():
            k = c[n] + j
            if i not in c or k < c[i]:
                c[i], d[i] = k, n
                heappush(b, (k + h.get(i, float('inf')), i))

    return None, float('inf')

g = {}
n1 = int(input("Enter the number of edges: "))
for _ in range(n1):
    u, v, w = input("Enter edge (start, end, weight): ").split()
    w = int(w)
    if u not in g:
        g[u] = {}
    g[u][v] = w
    if v not in g:
        g[v] = {}

h = {}
n2 = int(input("Enter the number of nodes with heuristics: "))
for _ in range(n2):
    node, heuristic = input("Enter node and heuristic: ").split()
    h[node] = int(heuristic)

s = input("Enter start node: ")
t = input("Enter target node: ")

e, f = a(g, h, s, t)
if e:
    print(f"Path: {e}, Distance: {f}")
else:
    print("Path not found.")
