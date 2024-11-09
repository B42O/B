def nq(n):
    # Error handling for invalid n values
    if n <= 0 or n == 2 or n == 3:
        print("No solution")
        return

    def q(s):
        if len(s) == n:
            for row in range(n):
                print(' '.join('Q' if col == s[row] else '.' for col in range(n)))
            print()
            return
        for c in range(n):
            if all(c != s[i] and abs(c - s[i]) != len(s) - i for i in range(len(s))):
                q(s + [c])

    q([])

n = int(input("Enter N: "))
nq(n)
