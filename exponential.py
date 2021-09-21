base=int(input("enter the value of x"))
exponent=int(input("enter the power of y"))
product=1
for i in range(1,exponent+1):
    product=product*base
print(base,"power",exponent,"is",product)
