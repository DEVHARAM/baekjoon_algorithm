import sys

n=int(input())
arr=[]
dp=[[0 for j in range(n)] for i in range(1,n+1)]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(i+1):
        if i==0:
            dp[i][j]=arr[i][j]
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+arr[i][j]
print(max(dp[n-1]))