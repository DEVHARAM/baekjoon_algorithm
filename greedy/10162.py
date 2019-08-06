n=int(input())
button=[300,60,10]
result=[0,0,0]
temp=n
for i in range(3):
    if button[i]>temp:
        continue
    result[i]=int(temp/button[i])
    temp=temp%button[i]
if temp!=0:
    print(-1)
else:
    print(' '.join(map(str,result)))
    