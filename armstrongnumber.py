'''This script used to find a number is armstrong or not'''
n = int(input("enter the number"))
temp = n
GUM = 0
while (n > 0):
    rem = n%10
    GUM = GUM +(rem*rem*rem)
    n = n//10
if (temp == GUM):
    print(GUM, "is an armstrong number")
else:
    print(GUM, "is not an armstrong number")
