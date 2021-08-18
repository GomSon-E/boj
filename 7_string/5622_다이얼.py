dict = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z'], }
a = input()
t = 0
for i in a:
    for key, value in dict.items():
        if i in value:
           t += key
print(t + len(a)) 