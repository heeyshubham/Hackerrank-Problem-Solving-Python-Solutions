def sockMerchant(n, ar):
    countsocks={}; pair=0;
    for element in ar:
        if(element in countsocks):
            countsocks[element]+=1
        else:
            countsocks[element]=1
    for value in countsocks.values():
        pair+=value//2
    return pair
