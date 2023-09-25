def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]),sum(arr[1:]))
    
    #METHOD2
    #
    # sum=0
    # for i in range(len(arr)):
    #     sum+=arr[i]
    # print ( sum-max(arr), sum-min(arr))
