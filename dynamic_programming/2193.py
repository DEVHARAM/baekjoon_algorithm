n=int(input())
memo=[0,1,1]
if n<=2:
    print(memo[n])
else:
    for i in range(3,n+1):
        memo.append(memo[i-1]+memo[i-2])
    print(memo[n])