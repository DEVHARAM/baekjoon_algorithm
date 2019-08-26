import sys
n=int(sys.stdin.readline())
sor=[0 for i in range(2000001)]
for i in range(n):
    num=int(sys.stdin.readline())
    sor[num+1000000]=1
for i in range(len(sor)):
    if sor[i]==1:
        print(i-1000000)