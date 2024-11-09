from collections import defaultdict
g = defaultdict(list)

def dl(n, goal, depth_limit, d=0):
    print(f"Visiting Node: {n}, Current Depth: {d}")
    if n == goal:
        return True
    if d >= depth_limit:
        return False
    for y in g.get(n, []):
        if dl(y, goal, depth_limit, d + 1):
            return True
    return False

def add_edge(x, y):
    g[x].append(y)

e = int(input("Enter number of edges: "))
for _ in range(e):
    x, y = map(int, input("Enter edge (from to): ").split())
    add_edge(x, y)

s = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))
dl_limit = int(input("Enter depth limit: "))

if dl(s, goal, dl_limit):
    print(f"Goal node {goal} found within depth limit {dl_limit}")
else:
    print(f"Goal node {goal} NOT found within depth limit {dl_limit}")
