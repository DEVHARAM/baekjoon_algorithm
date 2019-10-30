from itertools import permutations
from collections import deque
class country:
    def __init__(self,name,score=None,percentage=None):
        self.name=name
        self.score=score
        self.percentage=percentage

team=[]
def cases(li,k):
    global team
    if k==6:
        score=[0,0,0,0]
        percentage=[1,1,1,1]
        ind=0
        for i in range(len(team)):
            for j in range(3):
                score[i]+=team[i].score[ind]
                percentage[i]*=team[i].percentage[j][ind]
                ind+=1
        print(score)
        print(percentage)
            
        return
    for i in range(3):
        li.append(i)
        cases(li,k+1)
        li.pop()
cases(deque(),0)

coun=input().split()
for i in range(4):
    team.append(country(coun[i]))
for i in range(6):
    a,b,w,d,l=input().split()
    for t in team:
        if t.name==a:
            t.score=[3,1,0]
            if t.percentage==None:
                t.percentage=[[w,d,l]]
            else:
                t.percentage.append([w,d,l])
        elif t.name==b:
            t.score=[0,1,3]
            if t.percentage==None:
                t.percentage=[[l,d,w]]
            else:
                t.percentage.append([l,d,w])
        
            


        