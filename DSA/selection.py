def selection_sort(col):
    for pass_no in range(1,len(col)):
        min_pos=pass_no-1
        for i in range(pass_no,len(col)):
            if col[i]<col[min_pos]:
                min_pos=i
        col[pass_no-1],col[min_pos]=col[min_pos],col[pass_no-1]
    return col

l = ["bannana", "apple", "grapes", "watermelon"]
print(selection_sort(l))

# assume a min
# find real min
# swap real min and assumed min
