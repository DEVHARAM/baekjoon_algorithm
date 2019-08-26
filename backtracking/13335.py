import sys
from collections import deque


n,w,L=map(int,sys.stdin.readline().split())
truck=deque(list(map(int,sys.stdin.readline().split())))
w_ing=deque()
t_ing=deque()
time=0
while True:

    if not truck and not t_ing: break
    count=0
    for i in range(len(w_ing)):
        t_ing[i]+=1
        if t_ing[i]==w+1:
            count+=1
    for i in range(count):
        t_ing.popleft()
        w_ing.popleft()
    if truck:
        if truck[0]>L: truck.popleft()
        if sum(w_ing)+truck[0]<=L:
            w_ing.append(truck.popleft())
            t_ing.append(1)

    time+=1

print(time)