for consuer in range (5):
    lr=int(input("enter last month eletricity reading"))
    cr=int(input("enter last month eletricity reading"))
    cm=int(input("enter consumer number reading"))
    cd=cr-lr
    print("total eletricity consumption is",cd)
    if(cd>=1 and cd<=100):
        amount=cd*2
        print ("consumer number",cm)
        print("you have to pay",amount,"rupees")
    elif(cd>=100 and cd<=300):
        amount=cd*4
        print("you have to pay",amount,"rupees")
    elif(cd>=300):
        amount=cd*6
        print("you have to pay",amount,"rupees")
    else:
        print("wrong reading")

