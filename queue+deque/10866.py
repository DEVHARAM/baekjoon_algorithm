import sys
from collections import deque
que=deque()
for i in range(int(input())):
    command=sys.stdin.readline().split()

    if command[0]=='pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    if command[0]=='pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    if command[0]=='size':
        print(len(que))
    if command[0]=='empty':
        if que:
            print(0)
        else:
            print(1)
    if command[0]=='front':
        if que:
            print(que[0])
        else: 
            print(-1)
    if command[0]=='back':
        if que:
            print(que[len(que)-1])
        else: 
            print(-1) 
    if command[0]=='push_front':
        que.appendleft(command[1])
    if command[0]=='push_back':
        que.append(command[1])

    
        