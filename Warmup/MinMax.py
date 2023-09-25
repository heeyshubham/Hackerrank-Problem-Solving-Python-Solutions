def miniMaxSum(arr):
    arr.sort()
    minsum=sum(arr[:-1])
    maxsum=sum(arr[1:])
    print(minsum,maxsum)
    
    #METHOD2
    #
    # sum=0
    # for i in range(len(arr)):
    #     sum+=arr[i]
    # print ( sum-max(arr), sum-min(arr))
