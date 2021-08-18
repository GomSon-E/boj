alpb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()
for i in alpb:
    if i in w:
        w = w.replace(i, '0')
print(len(w))