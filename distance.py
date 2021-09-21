import math
def dist():
    x1=int(input("enter the number x1"))
    x2=int(input("enter the number x2"))
    y1=int(input("enter the number y1"))
    y2=int(input("enter the number y2"))
    a=math.sqrt(x2-x1)**2
    b=math.sqrt(y2-y1)**2
    c=math.sqrt(a*b)
    print("the distance of the two points",c)
dist()

