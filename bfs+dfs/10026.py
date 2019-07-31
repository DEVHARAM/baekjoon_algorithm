import sys
sys.setrecursionlimit(10**6)

from collections import deque
def bfs(x,y):
    visit[x][y]=True
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n: continue
        if visit[nx][ny]==True: continue
        if arr[nx][ny]==arr[x][y]:
            bfs(nx,ny)

dx=[0,-1,0,1]
dy=[-1,0,1,0]
n_count=0
y_count=0
n=int(input())
arr=[]
visit=[[False for i in range(n)] for j in range(n)]
for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            bfs(i,j)
            n_count+=1
for i in range(n):
    for j in range(n):
        if arr[i][j]=='G':
            arr[i][j]='R'
visit=[[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            bfs(i,j)
            y_count+=1
            
print('%d %d'%(n_count,y_count))
