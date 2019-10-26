def solution(N, stages):
    result=[0 for i in range(N+2)]
    fail=[]
    for i in stages:
        result[i]+=1
    for i in range(1,N+1):
        if sum(result[i:])==0:
            temp=0
        else:
            temp=result[i]/sum(result[i:])
        fail.append([i,temp])
    fail=sorted(fail,key=lambda x:x[1],reverse=True)
    answer=[]
    for f in fail:
        answer.append(f[0])
    return answer