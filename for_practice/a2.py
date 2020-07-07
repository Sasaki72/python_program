def a(a,b):
    total = 0
    for s in range(a, b + 1):
        total = total + s
    return total

w = a(1, 5)
print(w)