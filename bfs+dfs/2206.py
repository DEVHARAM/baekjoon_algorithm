import sys
from collections import deque
def bfs():
    while q:
        x,y,z=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if xx<0 or xx>=n or yy<0 or yy>=m: continue
            if dist[xx][yy][z]==-1 and arr[xx][yy]==0:
                q.append((xx,yy,z))
                dist[xx][yy][z]=dist[x][y][z]+1
            elif z==0 and dist[xx][yy][z+1]==-1 and arr[xx][yy]==1:
                q.append((xx,yy,z+1))
                dist[xx][yy][z+1]=dist[x][y][z]+1

dx=[-1,0,1,0]
dy=[0,-1,0,1]
n,m=map(int,input().split())
arr=[list(map(int,[*input()])) for k in range(n)]
dist=[[[-1]*2 for i in range(m)] for j in range(n)]
dist[0][0][0]=1
q=deque()
q.append((0,0,0))
bfs()
if dist[n-1][m-1][0]==-1:
    print(dist[n-1][m-1][1])
elif dist[n-1][m-1][1]==-1:
    print(dist[n-1][m-1][0])
else:
    print(min(dist[n-1][m-1]))

