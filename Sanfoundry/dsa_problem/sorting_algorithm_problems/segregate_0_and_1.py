def segregate(arr):
    left=0
    right=len(arr)-1

    while left<right:
        if arr[left]==0:
            left+=1
        elif arr[right]==1:
            right-=1
        else:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    print(arr)

arr=[0,1,0,1,0,0,1,1,1,0]
segregate(arr)
