def a(b, c, d, e):
    return all(c[i] != e for i in range(len(b)) if b[d][i])

def f(b, m, c, d=0):
    if d == len(b): return True
    for e in range(1, m + 1):
        if a(b, c, d, e):
            c[d] = e
            if f(b, m, c, d + 1): return True
            c[d] = 0
    return False

n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of colors: "))
b = [list(map(int, input().split())) for _ in range(n)]
c = [0] * n
if f(b, m, c):
    print("Coloring is possible:", c)
else:
    print("Coloring is not possible")
