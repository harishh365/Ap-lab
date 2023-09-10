l=[3,4,5,5,6,7,5,8]
item=int(input("Enter item to replace"))
newItem=int(input("Enter new-item to be replaced"))
if item in l:
    for i in range(len(l)):
        if(item==l[i]):
            l[i]=newItem
    print(l)
else:
    print("Not Found")