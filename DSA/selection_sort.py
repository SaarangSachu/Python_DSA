def selection_sort(col):
    for pass_num in range(1,len(col)):
        min_pos=pass_num-1
        for i in range(pass_num,len(col)):
            if col[i]<col[min_pos]:
                min_pos=i
        col[pass_num-1],col[min_pos]=col[min_pos],col[pass_num-1]
    return col
print(selection_sort([2,4,1,3,2]))
