def bonAppetit(bill, k, b):
    bact=sum(bill)
    bact=(bact-bill[k])//2
    if(bact==b):
        print("Bon Appetit")
    else:
        print(abs(bact-b))
