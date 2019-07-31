import sys
from collections import deque
left_data=deque()
right_data=deque()
i=list(input())
for a in i:
    left_data.append(a)
for j in range(int(input())):
    ed=sys.stdin.readline().strip()
    if ed=='L':
        if left_data:
            right_data.appendleft(left_data.pop())
    if ed=='D':
        if right_data:
            left_data.append(right_data.popleft())
        
    if ed=='B':
        if left_data:
            left_data.pop()
    if ed[0]=='P':
        left_data.append(ed[2])
    

print(''.join(left_data)+''.join(right_data))