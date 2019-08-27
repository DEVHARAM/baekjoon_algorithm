def solve(day,profit):
    global ans
    if day==n+1:
        if ans<profit:
            ans=profit
        return
    if day>n+1:
        return
    solve(day+T[day],profit+P[day])
    solve(day+1,profit)

n=int(input())
ans=0
T=[0]
P=[0]
for i in range(n):
    a,b=map(int,input().split())
    T.append(a)
    P.append(b)
solve(1,0)
print(ans)