n,m=map(int,input().split())
board=[]
tmp=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    board.append(list(input()))
for i in range(n):
    for j in range(m):
        if j+1<m and board[i][j]!=board[i][j+1]:
            tmp[i][j]=1
            tmp[i][j+1]=1
        if i+1<n and board[i][j]!=board[i+1][j]:
            tmp[i][j]=1
            tmp[i+1][j]=1
result=0
for i in range(n):
    for j in range(m):
        if tmp[i][j]==1:
            result+=1
print(pow(2,n*m-result)%1000000007)