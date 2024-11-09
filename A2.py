from collections import deque
def water_jug(x, y, t):
    v = set()  
    q = deque([(0, 0, [])]) 
    
    while q:
        a, b, s = q.popleft()
        if a == t or b == t:
            return s + [(a, b)] 
        if (a, b) in v:
            continue 
        v.add((a, b))
        q.extend([
            (x, b, s + [(a, b)]),  
            (a, y, s + [(a, b)]), 
            (0, b, s + [(a, b)]),  
            (a, 0, s + [(a, b)]),  
            (min(a + b, x), a + b - min(a + b, x), s + [(a, b)]), 
            (a + b - min(a + b, y), min(a + b, y), s + [(a, b)])   
        ])
    return "No solution"
x = int(input("Enter capacity of Jug 1: "))
y = int(input("Enter capacity of Jug 2: "))
t = int(input("Enter target amount: "))
sol = water_jug(x, y, t)
print("Solution:", sol)
