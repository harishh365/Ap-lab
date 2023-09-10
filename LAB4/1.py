l=[1,2,3,4,7,0]
c=[]
x=len(l)-1
n=int(len(l)/2)
for i in range(n):
    c.append(l[i])
    l[i]=l[x-i]
    l[x-i]=c[i]
print(l)
