import math
def check_prim(num):
    if num==1:return False
    n=int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:return False
    return True

n,m=map(int,input().split())
for i in range(n,m+1):
    if check_prim(i)==True: print(i)