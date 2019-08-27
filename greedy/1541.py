

import re
n=input()
if '-' not in n:
    a=list(map(int,n.split('+')))
    print(sum(a))
else: 
    t=n.index('-')
    a=list(map(int,n[:t].split('+')))
    b=list(map(int,re.split('\+|\-',n[t:])[1:]))
    print(sum(a)-sum(b))