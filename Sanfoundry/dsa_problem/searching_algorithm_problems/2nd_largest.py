def second_largest(arr):
    largest=0
    second=0

    for i in arr:
        if i> largest:
            second=largest
            largest=i
        elif i> second and i!=largest:
            second=i
    return second

arr=[10,20,301,4,11,33]
print(second_largest(arr))