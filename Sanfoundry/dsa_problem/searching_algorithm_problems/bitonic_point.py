def bitomic_point(arr):
    max=arr[0]

    for i in arr:
        if i> max:
            max=i

    return max

arr=[10,20,301,4,11,33]
print(bitomic_point(arr))