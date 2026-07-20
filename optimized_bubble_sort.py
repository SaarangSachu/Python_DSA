def bubble_sort(col):
    for pass_num in range(1,len(col)):
        swapped=False
        for i in range(len(col)-pass_num):
            if col[i]>col[i+1]:
                col[i],col[i+1]=col[i+1],col[i]
                swapped=True
        if swapped==False:
            break
    return col

print(bubble_sort([1,2,3,4]))
print(bubble_sort(['hello','good','king','bye','take','care']))
    