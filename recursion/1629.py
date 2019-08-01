def poww(a,b,c):
    if b==0: return 1
    val=poww(a,int(b/2),c)
    val=val*val%c
    if b%2==0: return val
    return val*a%c

a,b,c=map(int,input().split())
print(poww(a,b,c))