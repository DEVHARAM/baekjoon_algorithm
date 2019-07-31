sum=0
comp=[]
state=0
n=int(input())
st=[0]
for i in range(n):
    st.append(int(input()))
memo=[0]*(n+1)
memo[1]=st[1]
memo[2]=memo[1]+st[2]
for i in range(3,len(memo)):
    memo[i]=max(st[i]+memo[i-2],st[i]+memo[i-3]+st[i-1])
print(memo.pop())