def binary_search(col,key,li,hi):
    if li>hi:
        return -1
    mid=(li+hi)//2
    if col[mid]==key:
        return mid
    elif key<col[mid]:
        hi=mid-1
    else:
        li=mid+1
    return binary_search(col,key,li,hi)
col=[1,2,3,4,5]
print(binary_search(col,2,0,len(col)))