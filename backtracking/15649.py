def back(arr,use,k):
    if k==m: 
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if use[i]==False:
            arr[k]=i
            use[i]=True
            back(arr,use,k+1)
            use[i]=False
    
n,m=map(int,input().split())
use=[False for i in range(n+1)]
arr=[0 for i in range(m)]
back(arr,use,0)