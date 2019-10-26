def solution(record):
    command=[]
    info=dict()
    for r in record:
        r=r.split()
        
        if r[0]=="Enter":
            command.append(['enter',r[1]])
            info[r[1]]=r[2]
        elif r[0]=="Leave":
            command.append(['leave',r[1]])
        elif r[0]=="Change":
            info[r[1]]=r[2]
    result=[]
    for c in command:
        if c[0]=="enter":
            result.append(info[c[1]]+"님이 들어왔습니다.")
        elif c[0]=="leave":
            result.append(info[c[1]]+"님이 나갔습니다.")
    return result