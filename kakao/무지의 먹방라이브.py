def solution(food_times, k):
    info=[]
    temp=k
    remain=0
    for i in range(len(food_times)):
        info.append([i,food_times[i]])
    info=sorted(info,key=lambda x:x[1])
    for i in range(len(info)):
        remain=temp
        temp-=info[i][1]*(len(info)-i)
        if temp<=0:
            break   
        else:
            b=info[i][1]
            for j in range(i,len(info)):
                info[j][1]-=b
    info=sorted(info[i:],key=lambda x:x[0])
    return info[remain%len(info)][0]+1