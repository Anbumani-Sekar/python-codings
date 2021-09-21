a=[ ]
print("enter 5 values")
for i in range (0,5):
    x=int(input())
    a.append(x)
print(a)
pos=int(input("enter the position"))
value=int(input("enter the value"))
a[5]=a.append(0)
for i in range(5,pos-2,-1):
    a[i]=a[i-1]
a[pos-1]=value
print(a)
    
