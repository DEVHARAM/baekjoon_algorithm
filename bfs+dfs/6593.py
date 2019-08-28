from collections import deque
def bfs():
    q=deque()
    q.append(s)
    visit=[[[0 for k in range(C)] for j in range(R)] for i in range(L)]

    count=0
    while q:
        z,y,x=q.popleft()
        for i in range(6):
            nz,ny,nx=z+dz[i],y+dy[i],x+dx[i]
            if nz<0 or nz>=L or nx<0 or nx>=C or ny<0 or ny>=R: continue
            if visit[nz][ny][nx]: continue
            if building[nz][ny][nx]!='#':
                visit[nz][ny][nx]=visit[z][y][x]+1
                q.append((nz,ny,nx))
    finish=visit[e[0]][e[1]][e[2]]
    if finish!=0:
        print("Escaped in %d minute(s)."%finish)
    else: print("Trapped!")
    

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
while True:
    L,R,C=map(int,input().split())
    if L==0 and R==0 and C==0: break
    building=[]
    for j in range(L):
        building.append([list([*input()]) for k in range(R)])
        input()
    for i in range(L):
        for j in range(R):
            for l in range(C):
                if building[i][j][l]=='S':
                    s=(i,j,l)
                if building[i][j][l]=='E':
                    e=[i,j,l]                
    bfs()