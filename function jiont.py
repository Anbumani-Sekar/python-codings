#function with no arguments and no return value
def sum():
    n1=int(input("enter number n1="))
    n2=int(input("enter number n2="))
    sum=n1+n2
    print("Answer :",sum)
#function with  arguments and no return value
def sub(x,y):
    z=x-y
    print("Answer :",z)
#function with no arguments and return value
def mul():
    m1=int(input("enter number m1="))
    m2=int(input("enter number m2="))
    mul=m1*m2
    return(mul)
#function with  arguments and no return value
def div(x,y):
    z=x//y
    return(z)
sum()
s1=int(input("enter number s1="))
s2=int(input("enter number s2="))
sub(s1,s2)
print("ANSWER :",mul())
d1=int(input("enter number d1="))
d2=int(input("enter number d2="))
print(" Answer :",div(d1,d2))


