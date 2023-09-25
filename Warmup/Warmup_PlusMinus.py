from decimal import Decimal, getcontext
def plusMinus(arr):
    pos=neg=zero=0
    for i in range(len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        elif(arr[i]==0):
            zero+=1
    getcontext().prec = 6
    print(Decimal(pos)/Decimal(len(arr)))
    print(Decimal(neg)/Decimal(len(arr)))
    print(Decimal(zero)/Decimal(len(arr)))
