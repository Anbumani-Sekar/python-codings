list=[ ]
print("enter 5 values")
for i in range (0,5):
    x=(input())
    list.append(x)
print(list)
num=(input("enter the no; to be searched"))
for item in range (len(list)):
    if list[item]==num:
        print("item found at",(item+1))
        break
    else:
        print("item not found")
