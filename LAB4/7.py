l=[1,2,3,4]
item=int(input("Enter item after which new item to be added"))
ni=int(input("Enter item to be added"))
for i in range(len(l)):
    if(item==l[i]):
        l.insert(i+1,ni)
print(l)