from collections import deque
def bfs():
    q=deque()
    q.append(n)
    visit=[0 for i in range(100001)]
    path=[0 for i in range(100001)]
    result=[]
    while q:
        x=q.popleft()
        if x==k: 
            print(visit[k])
            while x!=n:
                result.append(x)
                x=path[x]
            result.append(n)
            result.reverse()
            print(' '.join(map(str,result)))
            return
        for nx in (x-1,x+1,x*2):
            if 0<=nx<=100000 and not visit[nx]:
                visit[nx]=visit[x]+1
                path[nx]=x
                q.append(nx)
    
n,k=map(int,input().split())
bfs()
