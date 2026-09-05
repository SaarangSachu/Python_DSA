def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr=[1,2,7,3,4,5,6]
print(is_sorted(arr))