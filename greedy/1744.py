import sys
from collections import deque
num=int(sys.stdin.readline())
min_arr=[]
plus_arr=[]
for i in range(num):
    temp=int(sys.stdin.readline())
    if temp<=0:
        min_arr.append(temp)
    else:
        plus_arr.append(temp)
min_arr=deque(sorted(min_arr))
plus_arr=deque(sorted(plus_arr,reverse=True))
result=0
while min_arr:
    if len(min_arr)>=2:
        a=min_arr.popleft()
        b=min_arr.popleft()
        result+=(a*b)
    else:
        result+=min_arr.popleft()
while plus_arr:
    if len(plus_arr)>=2:
        a=plus_arr.popleft()
        b=plus_arr.popleft()
        if a==1 or b==1:
            result+=(a+b)
        else:
            result+=(a*b)
    else:
        result+=plus_arr.popleft()
print(result)
