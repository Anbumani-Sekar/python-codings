def insertionsort(a):
    for index in range(1,len(a)):
        currentvalue=a[index]
        position=index
        while position>0 and a[position-1]>currentvalue:
            a[position]=a[position-1]
            position=position-1
            a[position]=currentvalue
a=[23,78,45,8,32,50]
insertionsort(a)
print("the sorted list using insertionsort is")
print(a)
