def fact():
    n=int(input("enter the number"))
    fact=1
    for i in range(1,n+1):
            fact=fact*i
    print("the factorial of",n,"! is",fact)
def fibon():
    print("fibonaci series")
    n=int(input("enter the limit:"))
    f1=-1
    f2=1
    for i in range(1,n+1):
          f3=f1+f2
          print(f3,end="\t")
          f1=f2
          f2=f3
def end():
    print("-------------------------------------")
    print("-------------------------------------")
fact()
end()
fibon()
    
