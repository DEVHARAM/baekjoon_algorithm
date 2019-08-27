import sys
n,k=map(int,input().split())
coin=[]
dp=[0 for i in range(k+1)]
for i in range(1,k+1):
    dp[i]=10001
for i in range(n):
    coin.append(int(sys.stdin.readline()))
for i in range(n):
    for j in range(coin[i],k+1):
        dp[j]=min(dp[j],dp[j-coin[i]]+1)
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])