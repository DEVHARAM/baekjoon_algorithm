n=int(input())
grape=[]
result=[[0 for i in range(2)] for j in range(n+1)]
for i in range(n):
    grape.append(int(input()))
for i in range(1,n+1):
    result[i][0]=max(result[i-1])
    if i>1:
        result[i][1]=max(result[i-2][0]+grape[i-1]+grape[i-2],result[i-1][0]+grape[i-1])
    else:
        result[i][1]=grape[i-1]
print(max(result[n]))