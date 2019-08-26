import sys
sys.setrecursionlimit(10**6)

def recur(i):
    global count
    global column_visit,diagonal_visit1,diagonal_visit2
    
    if i==n: 
        count+=1
        return
        
    for j in range(n):
        if  column_visit[j]==False and diagonal_visit1[i+j]==False and diagonal_visit2[i-j+n-1]==False:
            column_visit[j]=True
            diagonal_visit1[i+j]=True
            diagonal_visit2[i-j+n-1]=True
            recur(i+1)
            column_visit[j]=False
            diagonal_visit1[i+j]=False
            diagonal_visit2[i-j+n-1]=False
    
n=int(input())
column_visit=[False for i in range(n)]
diagonal_visit1=[False for i in range(n*2-1)]
diagonal_visit2=[False for i in range(n*2-1)]
count=0
recur(0)

print(count)

        
        
        