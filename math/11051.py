import sys
sys.float_info.max
n,k=map(int,input().split())
result=1
for i in range(k):
    result=result*(n-i)
if k!=0:
    for i in range(1,k+1):
        result=int(result//i)
    print(result%10007)
else:
    print(1)