num=int(input())
ball=[1,2,3]
for i in range(num):
    n,m=map(int,input().split())
    a=ball.index(n)
    b=ball.index(m)
    temp=ball[a]
    ball[a]=ball[b]
    ball[b]=temp
print(ball[0])