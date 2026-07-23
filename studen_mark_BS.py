def bubble_sort_by_marks(students):
    col = list(students)
    
    for pass_num in range(1, len(col)):
        swapped = False
        for i in range(len(col) - pass_num):
            if col[i][1] < col[i + 1][1]:
                col[i], col[i + 1] = col[i + 1], col[i]
                swapped = True
        if not swapped:
            break
            
    return col


students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(bubble_sort_by_marks(students))