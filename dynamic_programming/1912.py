n=int(input())
arr=[0]
arr+=list(map(int,input().split()))
li=[0 for j in range(n+1)]
result=-1001
for i in range(1,n+1):
    li[i]=max(li[i-1]+arr[i],arr[i])
    result=max(result,li[i])
    
print(result)