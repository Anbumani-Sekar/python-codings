def add(a,b):
    #a=int(input('enter age'))
    #b=int(input('enter epm id'))
    return a+b


def sub(d,r):
    #a=int(input('enter age'))
    #b=int(input('enter epm id'))
    print("subtraction",d-r)
def multi(t,u):
    #a=int(input('enter age'))
    #b=int(input('enter epm id'))
    print("multi",t*u)
def div(w,y):
    #a=int(input('enter age'))
    #b=int(input('enter epm id'))
    print("div",w/y)
count=0
for i in range(1,5):
    print("i is :",i)

    for j in range(1,5):
        print("j is :",j)

        for k in range(1,5):
            print("k is:",k)
            count+=1
            print(count)
        
