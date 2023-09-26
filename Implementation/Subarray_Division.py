def birthday(s, d, m):
    ways=0
    for i in range(len(s)):
        if((i+m-1)<len(s)):
            if(d==sum(s[i:i+m])):
                ways+=1
    return ways
