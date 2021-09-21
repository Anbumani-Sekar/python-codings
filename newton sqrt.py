def nesq(n):
    ap=0.5*n
    bet=0.5*(ap+n/ap)
    while(ap!=bet):
        ap=bet
        bet=0.5*(ap+n/ap)
        return bet
print(nesq(10))
