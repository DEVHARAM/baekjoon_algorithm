import itertools
def calculate(select):
    count=0
    com=itertools.permutations(list(select),2)
    for coms in com:
        count=count+arr[coms[0]][coms[1]]
    return count

        
def recur(k,start):
    if k==int(n/2):
        a=calculate(select)
        b=calculate(set(total)-set(select))
        if a>b:
            result.append(a-b)
        else: 
            result.append(b-a)
        return 
    for j in range(start,n):
        if visit[j]==False:
            select.append(j)
            visit[j]=True
            recur(k+1,j)
            select.remove(j)
            visit[j]=False

n=int(input())
arr=[]
total=[]
result=[]
for i in range(n):
    total.append(i)
select=[]
visit=[False for i in range(n)]

for i in range(n):
    arr.append(list(map(int,input().split())))
recur(0,0)
print(min(result))