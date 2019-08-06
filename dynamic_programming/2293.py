n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
d=[0 for i in range(k+1)]
d[0]=1
for i in a:
    for j in range(i,k+1):
        d[j]=d[j-i]+d[j]
print(d[k])