n=int(input())
color=[]
for i in range(n):
    color.append([0,0,0])

for i in range(n):
    if i==0:
        color[0]=list(map(int,input().split()))
    else: 
        r,g,b=map(int,input().split())
        if r+color[i-1][1]>r+color[i-1][2]:
            color[i][0]=r+color[i-1][2]
        else:
            color[i][0]=r+color[i-1][1]
        if g+color[i-1][0]>g+color[i-1][2]:
            color[i][1]=g+color[i-1][2]
        else:
            color[i][1]=g+color[i-1][0]        
        if b+color[i-1][0]>b+color[i-1][1]:
            color[i][2]=b+color[i-1][1]
        else:
            color[i][2]=b+color[i-1][0]
print(min(color[n-1]))