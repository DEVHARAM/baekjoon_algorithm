n=int(input())
li=[0 for i in range(n+1)]

for i in range(0,n+1):
    if i>n: break
    if i<=1:
        li[i]=0
    else:
        mint=n+1
        if i%3==0:
            mint=min(mint,li[int(i/3)])
        if i%2==0:
            mint=min(mint,li[int(i/2)])
        mint=min(mint,li[i-1])
        li[i]=mint+1
    

print(li[n])
    
