n,m=map(int,input().split())
MAX=100000
d=[-1]*(MAX+1)
q=[]
q.append(n)
d[n]=0
while q:
    x=q.pop(0)
    for nx in [x-1,x+1,x*2]:
        if 0<=nx and nx<=MAX and d[nx]==-1 :
            d[nx]=d[x]+1
            q.append(nx)
print(d[m])