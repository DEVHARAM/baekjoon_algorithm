n=int(input())
rec=[0,1,2,4]
for j in range(4,11):
    rec.append(rec[j-1]+rec[j-2]+rec[j-3])
for i in range(n):
    num=int(input())
    print(rec[num])