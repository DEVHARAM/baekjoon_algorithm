def recur(k):
    global result
    if k==m:
        print(' '.join(map(str,result)))
        return
    for j in range(len(arr)):
        result[k]=arr[j]
        recur(k+1)
   
 
n,m=map(int,input().split())
result=[0 for i in range(m)] 
temp=sorted(list(map(int,input().split())),reverse=True)
temp2=[0 for i in range(temp[0]+1)]
arr=[]
for i in temp:
    temp2[i]+=1
for i in range(len(temp2)):
    if temp2[i]!=0:
        arr.append(i)

recur(0)