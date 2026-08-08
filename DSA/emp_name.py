def bubble_sort_by_name(employees):
    col = list(employees)
    
    for pass_num in range(1, len(col)):
        swapped = False
        for i in range(len(col) - pass_num):
            if col[i][0] > col[i + 1][0]:
                col[i], col[i + 1] = col[i + 1], col[i]
                swapped = True
        if not swapped:
            break
            
    return col

employees = [("John", 50000), ("Emma", 65000), ("Mike", 45000)]
print(bubble_sort_by_name(employees))