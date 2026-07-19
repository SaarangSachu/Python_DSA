def binary_search(col,key):
    least_index=0
    highest_index=len(col)-1
    while least_index<=highest_index:
        mid=(least_index+highest_index)//2
        if col[mid]==key:
            return mid
        elif key<col[mid]:
            highest_index=mid-1
        else:
            least_index=mid+1

print(binary_search([1,2,3,4,5,6,7,8,9,10],3))
print(binary_search([10,20,30,40],40))