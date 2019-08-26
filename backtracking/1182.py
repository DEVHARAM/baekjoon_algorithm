import sys
sys.setrecursionlimit(10**6)

def recur(start,k):
    global count,num,result

    if k==num:
        if result==m:
            count+=1
            return
        return

    for j in range(start,n):
        if visit[j]==False:
            visit[j]=True
            result+=arr[j]
            recur(j,k+1)
            visit[j]=False
            result-=arr[j]
count=0
result=0
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
visit=[False for i in range(n)]
for num in range(1,n+1):
    recur(0,0)
print(count)