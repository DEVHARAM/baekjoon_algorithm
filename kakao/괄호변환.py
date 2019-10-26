result=[]
def transfer(p):
    if len(p)==0:
        return
    set=0
    flag=False
    u=[]
    v=[]
    for i in range(len(p)):
        if p[i]=="(": 
            if set==0: flag=True
            set+=1
        elif p[i]==")": set-=1
        if set==0:
            u=p[:i+1]
            v=p[i+1:]
            break
    if flag==True:
        for ut in u:
            result.append(ut)
        transfer(v)
    else:
        result.append("(")
        transfer(v)
        result.append(")")
        if len(u)!=0:
            del u[0]
        if len(u)!=0:
            u.pop()
        for i in u:
            if i=="(":
                result.append(")")
            else:
                result.append("(")


def solution(p):
    p=list(p)
    
    if len(p)==0: 
        return p
    transfer(p)
    a="".join(result)
    return a