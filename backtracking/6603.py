def back(arr,use,k,start):
    global li
    if k==6: 
        result=[]
        for i in arr:
            result.append(li[i-1])
        print(' '.join(map(str,result)))
        return
    for i in range(start,n+1):
        if use[i]==False:
            arr[k]=i
            use[i]=True
            back(arr,use,k+1,i+1)
            use[i]=False
    
li=[]
while True:
    temp=list(map(int,input().split()))
    li=[]
    for i in range(len(temp)):
        if i==0:
            n=temp[i]
        else: 
            li.append(temp[i])
    if n==0: break
    use=[False for i in range(n+1)]
    
    arr=[0 for i in range(6)]
    back(arr,use,0,1)
    print()