def dp(num):
    if num == 1: return 1
    if num == 2: return 2
    if d[num]!=0: return d[num]
    d[num] = (dp(num-1)+dp(num-2))%10007
    return d[num]
d=[0]*1001
num=int(input())
print(dp(num))