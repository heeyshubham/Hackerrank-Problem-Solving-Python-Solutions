def getMoneySpent(keyboards, drives, b):
    #Alternative
    # return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])
    maxamount=0
    for i in range (len(keyboards)-1, -1, -1):
        for j in range(len(drives)-1, -1, -1):
            if(keyboards[i]+drives[j]<=b and maxamount<keyboards[i]+drives[j]):
                maxamount=keyboards[i]+drives[j]
    if(maxamount):
        return maxamount
    else:
        return -1
  
