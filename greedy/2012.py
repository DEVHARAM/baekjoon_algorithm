import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr=sorted(arr)
result=0
for i in range(n):
    if i+1<arr[i]:
        result=result+arr[i]-(i+1)
    else:
        result=result+(i+1)-arr[i]
print(result)