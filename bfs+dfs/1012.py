import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    mapp[x][y]=0
    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if a>=m or a<0 or b>=n or b<0: continue
        if mapp[a][b]:
            dfs(a,b)
    return
test=int(input())
dx=[-1,0,1,0]
dy=[0,-1,0,1]
m=n=k=0
mapp=[]
for d in range(test):
    ans=0
    m,n,k=map(int,input().split())
    mapp=[[0 for j in range(n+1)] for i in range(m+1)]

    for j in range(k):
        x,y=map(int,input().split())
        mapp[x][y]=1

    for j in range(m):
        for l in range(n):
            if mapp[j][l]:
                ans+=1
                dfs(j,l)
    print(ans)