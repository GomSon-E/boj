w = input().upper()
dict = {}
lst = []

for i in w:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for key, value in dict.items():
    if value == max(dict.values()):
        lst.append(key)

if len(lst) > 1:
    print('?')
else:
    print(lst[0])
