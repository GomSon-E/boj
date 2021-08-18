n = int(input())
ans = 0
for _ in range(n):
    w = input()
    stack = []
    idx = 0
    isGroup = 0
    for i in w:        
        if i not in stack:
            stack.append(i)
        else:
            if stack[idx-1] == i:
                stack.append(i)
            else:
                isGroup = 1
                break            
        idx += 1
    if isGroup == 0:
        ans += 1
print(ans)