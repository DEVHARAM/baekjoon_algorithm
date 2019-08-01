from collections import deque  
dx=[0,-1,0,1]
dy=[-1,0,1,0]

n,m=map(int,input().split())
count=[[1 for i in range(m)] for j in range(n)]
visit=[[False for i in range(m)] for j in range(n)]
arr=[list(map(int,list(input()))) for i in range(n)]
q=deque()
q.append((0,0))
count[0][0]=1
while q:   
    x,y=q.popleft()
    
    for i in range(4):          
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if visit[nx][ny]==False and arr[nx][ny]==1:
            count[nx][ny]=count[x][y]+1
            q.append((nx,ny))
            visit[nx][ny]=True
print(count[n-1][m-1])