def bubble_sort(col):
    count=0
    for pass_num in range(1,len(col)):
        swapped=False
        for i in range(len(col)-pass_num):
            if col[i]>col[i+1]:
                col[i],col[i+1]=col[i+1],col[i]
                swapped=True
                count+=1
        if swapped==False:
            break
    print("the count of swap is ",count)
    return col

print(bubble_sort([1,2,3,4]))
    