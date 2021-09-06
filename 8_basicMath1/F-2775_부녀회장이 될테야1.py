def People (k, n):
    if k == 1:
        return sum(range(n+1))
    else:
        return People(k-1, n)

print(People(1, 3))
