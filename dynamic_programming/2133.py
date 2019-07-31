def dp(num):
    if num == 0: return 1
    if num == 1: return 0
    if num == 2: return 3
    if d[num]!=0: return d[num]
    
    result=3*dp(num-2)
    for i in range(3,num+1,1):
        if i%2==0:
            result+=2*dp(num-i)
    d[num]=result
    return d[num]
d=[0]*31
num=int(input())
print(dp(num))