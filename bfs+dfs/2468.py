import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    check[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=h or ny<0 or ny>=h:
            continue
        if check[nx][ny]==0:
            dfs(nx,ny)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
maxi=0
h=int(input())
a = [list(map(int,list(input().split()))) for _ in range(h)]

for height in range(100):
    count=0
    check=[[0 for i in range(h)] for j in range(h)]
    for i in range(h):
        for j in range(h):
            if a[i][j]<=height:
                check[i][j]=1

    for i in range(h):
        for j in range(h):
            if check[i][j]==0:
                dfs(i,j)
                count+=1
    if maxi<count: maxi=count
print(maxi)