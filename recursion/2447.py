import math

def fractal(n):
    if n==3:
        return ['***','* *','***']
    s=fractal(int(n/3))
    temp=['' for j in range(n)]
    j=0
    for i in range(n):
        if int(n/3)<=i<int(n/3)*2:
            temp[i]=(s[j]+" "*int(n/3)+s[j])
        else:
            temp[i]=s[j]*3
        j+=1
        if j==len(s): j=0
    return temp
        
n = int(input())
k = int(math.log(n, 3))

result=fractal(n)
for i in result:
    print(i)
