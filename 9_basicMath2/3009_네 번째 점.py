import collections as c

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

x = [a1, b1, c1]
y = [a2, b2, c2]

print(c.Counter(x).most_common()[-1][0], c.Counter(y).most_common()[-1][0])
