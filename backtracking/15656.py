def back(arr,use,k):
    if k==m: 
        print(' '.join(map(str,arr)))
        return
    for i in range(0,n):
        arr[k]=li[i]
        back(arr,use,k+1)
       
            
    
n,m=map(int,input().split())
li=list(map(int,input().split()))
li=sorted(li,key=lambda x:x)
use=[False for i in range(n+1)]
arr=[0 for i in range(m)]

back(arr,use,0)