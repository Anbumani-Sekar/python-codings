A=[23,78,45,8,32,56]
for i in range(0,len(A)):
    min=i
    for j in range(i+1,len(A)):
        if A[min]>A[j]:
            min=j
    temp=A[i]
    A[i]=A[min]
    A[min]=temp
print("sorted list using selection sort is")
print(A)
