t = int(input())
for _ in range(t):
  x = 1
  h, w, n = map(int, input().split())
  while 1:
    if n > h:
      x += 1
      n -= h
    else:
      if x < 10:
        print(str(n)+'0'+str(x))
      else:
        print(str(n)+str(x))
      break
