def two_sum(l,target):
    d={}
    for i in range(len(l)):
        diff=target-l[i]
        if diff in d:
            return [d[diff],i]
        d[l[i]]=i

l=[3,4,2,8,7,1]
target=11

print(two_sum(l,target))