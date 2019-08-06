def prime(n):
    state=[True for i in range(n+1)]
    ret=[]
    state[1]=False
    for i in range(2,n+1):
        if state[i]==False: continue
        for j in range(i*i,n+1,i):
            state[j]=False
    for i in range(1,n+1):
        if state[i]:
            ret.append(i)
    return ret
        
n=int(input())
p=prime(n)
for i in range(len(p)):
    while True:
        if n%p[i]==0:
            print(p[i])
            n=n/p[i]
        else:
            break
