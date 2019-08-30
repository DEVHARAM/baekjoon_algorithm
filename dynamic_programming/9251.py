array1=list(input())
array2=list(input())

dp=[[0 for i in range(1002)] for j in range(1002)]
for i in range(1,len(array1)+1):
    for j in range(1,len(array2)+1):
        if array1[i-1]==array2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[len(array1)][len(array2)])