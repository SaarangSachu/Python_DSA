def binary_search(col, key, least_index=0, highest_index=None):
    # Initialize highest_index on the very first call
    if highest_index is None:
        highest_index = len(col) - 1
        
    # Base Case 1: If the indices cross, the key is not in the list
    if least_index > highest_index:
        return None
        
    mid = (least_index + highest_index) // 2
    
    # Base Case 2: Key is found
    if col[mid] == key:
        return mid
        
    # Recursive Step: Key is in the left half
    elif key < col[mid]:
        return binary_search(col, key, least_index, mid - 1)
        
    # Recursive Step: Key is in the right half
    else:
        return binary_search(col, key, mid + 1, highest_index)

# Your original test cases will work exactly the same way
print(binary_search([1,2,3,4,5,6,7,8,9,10], 3))
print(binary_search([10,20,30,40], 40))