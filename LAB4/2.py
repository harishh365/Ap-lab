a=[1,2,3,4]
b=[5,6,7]
s=[]
c=len(a)
d=len(b)
l=max(c,d)
for i in range(0,l):
    if(i<c):
        s.append(a[i])
    if(i<d):
        s.append(b[i])
print(s)