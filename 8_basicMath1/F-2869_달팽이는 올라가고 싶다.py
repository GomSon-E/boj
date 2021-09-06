a, b, v = map(int, input().split())
h = 0
day = 0

while 1:
    day += 1
    h += a
    if h >= v : break
    h -= b
    if h >= v: break

print(day)

# 시간초과