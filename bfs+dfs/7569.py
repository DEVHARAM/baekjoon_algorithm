from collections import deque
def bfs():
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            nz,nx,ny=z+dz[i],x+dx[i],y+dy[i]
            if 0<=nz<h and 0<=nx<m and 0<=ny<n and s[nz][nx][ny]==-1 and tomato[nz][nx][ny]==0:
                s[nz][nx][ny]=s[z][x][y]+1
                q.append((nz,nx,ny))

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
n,m,h=map(int,input().split())
tomato=[]
s=[[[-1]*n for i in range(m)]for j in range(h)]
for i in range(h):
    temp=[]
    for j in range(m):
        temp.append(list(map(int,input().split())))
    tomato.append(temp)
q=deque()
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k]==1:
                q.append((i,j,k))
                s[i][j][k]=0
bfs()
ans,flag=0,0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k]!=-1 and s[i][j][k]==-1: flag=-1
            ans=max(ans,s[i][j][k])
if flag==-1: print(-1)
else: print(ans)

            