l=[3,4,5,6,7,5,8]
item=int(input("Enter the item to be removed"))
for i in l:
        if(item==i):
            l.remove(i)
print(l)
