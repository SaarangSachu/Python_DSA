def find_floor(arr,x):
    ans=-1
    for i in range(len(arr)):
        if arr[i]<=x:
            ans=arr[i]
        else:
            break
    return ans

arr=[1,2,3,4,5,6,7,8,9,10]
x=7

print(find_floor(arr,x))