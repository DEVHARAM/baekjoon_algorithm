from collections import deque

N,K=map(int,input().split())
plug=deque(list(map(int,input().split())))
stack=[]
maxi=0
count=0
change=False
while plug:
    
    temp=plug.popleft()
    if temp in stack:
        continue
    if len(stack)!=N:
        stack.append(temp)
        continue
    else:
        change=False
        maxi=0
        for m in stack:
            if m in plug:
                if maxi<plug.index(m):
                    maxi=plug.index(m)
            else:
                stack[stack.index(m)]=temp
                count+=1
                change=True
                break
        if change==False:
            stack[stack.index(plug[maxi])]=temp
            count+=1

print(count)
