def hanoi(a,b,n):
    if n==1:
        print('%d %d'%(a,b))
        return
    c=6-a-b
    hanoi(a,c,n-1)
    print('%d %d'%(a,b))
    hanoi(c,b,n-1)
n=int(input())
print(pow(2,n)-1)
hanoi(1,3,n)