doc=input()
search=input()
count=0
temp=doc.find(search)
if temp!=-1:
    count+=1
while True:
    temp=doc.find(search,temp+len(search),len(doc))
    if temp==-1:
        break
    else:count+=1
print(count)