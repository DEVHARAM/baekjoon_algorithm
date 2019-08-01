from collections import deque
from collections import Counter
def back(c):
    global result
    if c==m: 
        print(' '.join(map(str,q)))
        return
    for i in range(len(cnt)):
        if cnt[i]:
            cnt[i]-=1
            q.append(arr[i])
            back(c+1)
            q.pop()
            cnt[i]+=1
       
            
q=deque()
n,m=map(int,input().split())
li=sorted(list(map(int,input().split())))
arr,cnt=map(list,zip(*sorted(list(Counter(li).items()))))

back(0)
