n=int(input())
dp=[[0 for i in range(10)] for j in range(n+1)]
for i in range(10):
    dp[0][i]=1
for i in range(n+1):
    for j in range(10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
print(dp[n][9]%10007)
