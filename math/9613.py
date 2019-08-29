import itertools
def gcd(a,b):
    if a<b:
        temp=b
        b=a
        a=temp
    for i in range(b,0,-1):
        if a%i==0 and b%i==0: return i        
for t in range(int(input())):
    temp=list(map(int,input().split()))
    n=temp[0]
    sum_gcd=0
    arr=[]
    for i in range(1,n+1):
        arr.append(temp[i])
    perm=list(itertools.combinations(arr,2))
    for i,j in perm:
        sum_gcd+=gcd(i,j)
    print(sum_gcd)
    
    