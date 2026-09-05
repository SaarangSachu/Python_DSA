def count_of_zero(arr):
    count=0
    for i in arr:
        if i==0:
            count+=1

    return count

print(count_of_zero([1,1,1,0,0,0,1,1,0]))