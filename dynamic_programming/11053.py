n=int(input())
arr=list(map(int,input().split()))

result=[0 for i in range(n)]
for i in range(n):
    result[i]=1
    for j in range(i):
        if arr[j]<arr[i]:
            result[i]=max(result[i],result[j]+1)
      
print(max(result))
        