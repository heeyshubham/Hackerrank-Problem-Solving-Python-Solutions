def migratoryBirds(arr):
    bpair={};
    for element in arr:
        if(element in bpair):
            bpair[element]+=1
        else:
            bpair[element]=1
    max_count=max(bpair.values())
    return min([bird for bird, count in bpair.items() if count == max_count])
