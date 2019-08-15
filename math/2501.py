n,m=map(int,input().split())

count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        if count==m:
            print(i)
            break
       
if count<m:
    print(0)