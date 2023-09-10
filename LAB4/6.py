l=["abc","lmn",""]
for i in l:
    if(i==""):
        l.remove("")
print(l)