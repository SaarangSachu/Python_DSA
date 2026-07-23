def sort_by_names(students):
    col = list(students)
    for pass_num in range(1, len(col)):
        swapped = False
        for i in range(len(col) - pass_num):
            # Using '>' puts names in alphabetical order
            if col[i][0] > col[i + 1][0]:
                col[i], col[i + 1] = col[i + 1], col[i]
                swapped = True
        if not swapped:
            break
    return col

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(sort_by_names(students))