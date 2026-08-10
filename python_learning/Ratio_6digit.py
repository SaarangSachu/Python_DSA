def ratio_of_positive_negative_zero(arr):
    positive_count=0
    negative_count=0
    zero_count=0
    lenght_arr=len(arr)
    for i in range(lenght_arr):
        if arr[i]>0:
            positive_count+=1
        elif arr[i]<0:
            negative_count+=1
        else:
            zero_count+=1
    print(f"{positive_count/lenght_arr:.6f}")
    print(f"{negative_count/lenght_arr:.6f}")
    print(f"{zero_count/lenght_arr:.6f}")


arr=[1,1,0,-1,-1]
ratio_of_positive_negative_zero(arr)