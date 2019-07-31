import sys
from collections import deque
def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny]==-1:
                continue
            if arr[nx][ny]:
                continue
            arr[nx][ny]=arr[x][y]+1
            q.append((nx,ny))
def solve():
    bfs()
    ans = 0
    for i in range(n):
        if 0 in arr[i]:
            return -1
        ans = max(ans, max(arr[i]))
    return ans-1


dx=[-1,0,1,0]
dy=[0,-1,0,1]
m,n=map(int,sys.stdin.readline().split())
arr=[]
q=deque()
for i in range(n):
    arr.append(list(map(int,list(sys.stdin.readline().split()))))
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j))
print(solve())