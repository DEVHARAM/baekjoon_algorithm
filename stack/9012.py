from collections import deque
for i in range(int(input())):
    stack=deque()
    arr=list(input())
    for i in arr:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                stack.append('(')
                break
            
    if stack:
        print('NO')
    else:
        print('YES')
    