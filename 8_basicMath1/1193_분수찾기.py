n = int(input())
idx = 1

while n > idx:
    n -= idx
    idx += 1

if idx % 2 == 0:
    if n == 1:
        print(str(n) + '/' + str(idx))
    else:
        print(str(n) + '/' + str(idx - (n-1)))
else:
    if n == 1:
        print(str(idx) + '/' + str(n))
    else:
        print(str(idx - (n-1)) + '/' + str(n))
