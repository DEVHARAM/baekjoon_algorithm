from collections import deque
def bfs():
    q=deque()
    q.append(n)
    visit=[0 for i in range(100001)]
    while q:
        x=q.popleft()
        if x==k:
            print(visit[k])
            break
        for nx in (x*2,x-1,x+1):
            if 0<=nx<=100000 and not visit[nx]:
                if nx==x*2:
                    visit[nx]=visit[x]
                    q.append(nx)
                else:
                    visit[nx]=visit[x]+1
                    q.append(nx)
    
n,k=map(int,input().split())
bfs()
