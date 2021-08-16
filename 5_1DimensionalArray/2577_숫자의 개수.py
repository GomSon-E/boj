a = int(input())
b = int(input())
c = int(input())

abc = str(a * b * c)
list = []
cnt = 0

for i in range(10):
    for j in abc:
        if str(i) == j:
            cnt += 1
    print(cnt)
    cnt = 0

