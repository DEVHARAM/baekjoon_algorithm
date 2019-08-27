import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
dp=[0 for i in range(m)]
for i in range(n):
    for j in range(m):
        if j==0:
            dp[j]+=arr[i][j]
        else:
            dp[j]=max(dp[j-1],dp[j])+arr[i][j]
print(dp[m-1])