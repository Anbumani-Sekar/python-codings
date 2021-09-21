def bs(sortedlist,n,x):
    first=0
    last=n-1
    while (first<=last):
        mid=(first+last)//2
        if(x==sortedlist[mid]):
            return mid
        elif(x<=sortedlist[mid]):
            last=mid-1
        else:
            first=mid+1
    return-1
n=int(input("enter the size of list"))
sortedlist=[ ]
for i in range(0,n):
    e=int(input("enter the list elements"))
    sortedlist.append(e)
x=int(input("enter the no; to search"))
position=bs(sortedlist,n,x)
if (position!=-1):
    print("entered no; is present at position:",(x,position))
else:
    print("entered no; is not present in list:")
    
