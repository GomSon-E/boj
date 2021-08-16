import string
s = input()
for i in string.ascii_lowercase:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')
