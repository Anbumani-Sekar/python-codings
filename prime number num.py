a=int(input("enter the limit range"))
count=0
for j in range(1,a+1):
    for i in range(1,a+1):
        r=j%i
        if (r==0):
            count=count+1
    if(count==2):
        print("prime no ",j)
    
        
