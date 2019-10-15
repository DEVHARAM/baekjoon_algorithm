n,m,h=map(int,input().split())
dx=[0,-1,0,1]
dy=[-1,0,1,0]
visit=[[False]*n for k in range(n)]
arr=[[0 for i in range(n)] for j in range(h)]
ans=4
def check():
    for i in range(n):
        k=i
        for j in range(h):
            if arr[j][k]: k+=1
            elif k>0 and arr[j][k-1]:
                k-=1
        if i!=k: return False
    return True
            
    
def solve(cnt,x,y):
    global ans
    if ans<=cnt: return
    if check():
        ans=min(ans,cnt)
        return
    if cnt==3: return
    for i in range(x,h):
        if i==x: k=y
        else: k=0
        for j in range(k,n-1):
            if arr[i][j]: j+=1
            else: 
                arr[i][j]=1
                solve(cnt+1,i,j+2)
                arr[i][j]=0
        
    
for i in range(m):
    x,y=map(int,input().split())
    arr[x-1][y-1]=1
solve(0,0,0)
print(ans if ans<4 else -1)
