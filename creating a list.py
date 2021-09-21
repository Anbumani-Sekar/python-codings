a=[ ]
b=[2,4,6,7,9]
print("enter 5 values")
for i in range (0,10):
    x=int(input())
    a.append(x)
print(a)
val=0
for j in range(len(b)):
    b1=b[j]
    c1=b1-1
    a1=a[c1]
    add=a1+val
    val=add
    print(val)
    
