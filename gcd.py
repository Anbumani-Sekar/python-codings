def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter a value"))
b=int(input("enter b value"))
Gcd=gcd(a,b)
print("Gcd is",Gcd)
