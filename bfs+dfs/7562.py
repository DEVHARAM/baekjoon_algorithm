from collections import deque
def bfs():
    q=deque()
    q.append((s_x,s_y))
    while q:
        x,y=q.popleft()
        if x==d_x and y==d_y:
            print(d[x][y])
            return
      
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            if d[nx][ny]==0:
                d[nx][ny]=d[x][y]+1
                q.append((nx,ny))
        
    
dx=[-1,1,-1,1,-2,2,-2,2]
dy=[-2,-2,2,2,-1,-1,1,1]

test=int(input())
for i in range(test):
    n=int(input())
    s_x,s_y=map(int, input().split())
    d_x,d_y=map(int, input().split())
    d=[[0 for j in range(n)] for i in range(n)]
    bfs()
