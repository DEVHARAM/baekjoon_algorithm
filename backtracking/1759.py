import sys
sys.setrecursionlimit(10**6)

def recur(result,visit,k,start):
    global a_check,b_check
    if L==k:
        if a_check>=1 and b_check>=2:
            print(''.join(result))
            return
        return
            
    for j in range(start,C):
        if visit[j]==False:
            result[k]=arr[j]
            visit[j]=True
            if arr[j] in ['a','e','i','o','u']:
                a_check+=1
            else:
                b_check+=1
            recur(result,visit,k+1,j)
            if arr[j] in ['a','e','i','o','u']:
                a_check-=1
            else:
                b_check-=1
            visit[j]=False


L,C=map(int,input().split())
a_check=0
b_check=0
arr=input().split()
arr=sorted(arr)
visit=[False for i in range(C+1)]
result=['' for i in range(L)]
recur(result,visit,0,0)


        
        
        