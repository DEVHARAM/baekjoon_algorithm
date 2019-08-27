
for t in range(int(input())):

    n=int(input())
    arr=[]
    for i in range(2):
        arr.append(list(map(int,input().split())))
    r=[[0 for i in range(n)] for j in range(2)]
    for i in range(n):
        if i==0:
            r[1][i]=arr[0][i]
            r[0][i]=arr[1][i]
        r[1][i]=max(r[0][i-1]+arr[1][i],r[0][i-2]+arr[1][i])
        r[0][i]=max(r[1][i-1]+arr[0][i],r[1][i-2]+arr[0][i])
    print(max(r[0][n-1],r[1][n-1]))

