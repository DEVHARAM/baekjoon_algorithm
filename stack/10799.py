from collections import deque
arr=list(input())
stack=deque()
result=0
for i in range(len(arr)):
    if arr[i]=='(':
        stack.append(arr[i])
    elif arr[i]==')':
        if stack:
            if arr[i-1]=='(':
                #·¹ÀÌÀú
                stack.pop()
                result+=len(stack)
               
            elif arr[i-1]==')':
                stack.pop()
                result+=1
print(result)