def div(r_start,r_end,c_start,c_end,num):
    if r==r_start and c==c_start:
        print(num)
        return
    r_mid=(r_start+r_end)//2
    c_mid=(c_start+c_end)//2
    
    n=(r_mid-r_start)*(c_mid-c_start)
    
    if r_start<=r<r_mid and c_start<=c<c_mid:
        div(r_start,r_mid,c_start,c_mid,num)
    elif r_start<=r<r_mid and c_mid<=c<c_end:
        div(r_start,r_mid,c_mid,c_end,num+n)
    elif r_mid<=r<r_end and c_start<=c<c_mid:
        div(r_mid,r_end,c_start,c_mid,num+(n*2))    
    elif r_mid<=r<r_end and c_mid<=c<c_end:
        div(r_mid,r_end,c_mid,c_end,num+(n*3))        

n,r,c=map(int,input().split())
po=2**n
div(0,po,0,po,0)

