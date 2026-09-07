def intersection(arr1,arr2):
    i=0
    j=0
    result=[]

    while i< len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            # if len(result)==0 or arr1[i] not in result:
            #     result.append(arr1[i])
            if len(result)==0 or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
            j+=1

    return result 

a=[1,2,2,3,4]
b=[2,2,4,5]


print(intersection(a,b))
 