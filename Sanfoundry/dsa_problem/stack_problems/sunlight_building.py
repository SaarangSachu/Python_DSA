def countBuilding(arr):
    count=0
    max_height=0
    for height in arr:
        if height>=max_height:
            count+=1
            max_height=height
    return count

print(countBuilding([2,1,3,2,4,6]))