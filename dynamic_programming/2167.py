import sys

n,m=map(int,input().split())
arr=[[0 for i in range(m+1)]]
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n):
    temp=list(map(int,input().split()))
    temp2=[0]
    for j in temp:
        temp2.append(j)
    arr.append(temp2)
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]+arr[i][j]-dp[i-1][j-1]
for t in range(int(input())):
    i,j,x,y=map(int,input().split())
    print(dp[x][y]-(dp[i-1][y]+(dp[x][j-1]-dp[i-1][j-1])))