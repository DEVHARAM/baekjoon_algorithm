import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global si
    visit[x][y]=True
    arr[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if arr[nx][ny]==1 and visit[nx][ny]==False: 
            si+=1
            dfs(nx,ny)
    
dx=[0,-1,0,1]
dy=[-1,0,1,0]
count=0
si=0
ma=0
n,m=map(int,input().split())
visit=[[False for i in range(m)] for j in range(n)]
arr=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and visit[i][j]==False:
            si+=1
            dfs(i,j)
            if ma<si: ma=si
            si=0
            count+=1

print(count)
print(ma)