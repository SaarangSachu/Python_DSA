def first_repeating_element(arr):
    for i in range(len(arr)):
        if arr[i] in arr[i+1:]:
            return arr[i]

    return -1

print(first_repeating_element([10,11,20,4,4,11,33]))