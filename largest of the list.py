n=int(input(":enter the limit"))
list=[]
print("enter list elements one by one")
for i in range (0,n):
    x=int(input())
    list.append(x)
print(list)
large=list[0]
for i in range(1,n):
    if (list[i]> large):
        large=list[i]
print("the largest number in the list,",large)
