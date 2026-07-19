def count_list(coll,key):
    count=0
    for i in range(len(coll)):
        if key==coll[i]:
            count+=1
    return count
    

print(count_list([1,2,3,4,1,2,1,2,4,1,2],1))
