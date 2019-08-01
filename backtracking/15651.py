def back(arr,k):
    if k==m: 
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        arr[k]=i
        back(arr,k+1)
    
n,m=map(int,input().split())
arr=[0 for i in range(m)]
back(arr,0)