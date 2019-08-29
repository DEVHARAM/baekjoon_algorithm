def check_prim(i):
    n=i*i
    if n==1: return False
    for j in range(2,n+1):
        if j==i: continue
        if i%j==0: 
            return False
    return True
            

num=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if check_prim(i)==True: count+=1
print(count)