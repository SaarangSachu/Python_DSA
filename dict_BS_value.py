def bubble_sort_dict_by_value(my_dict):
    col = list(my_dict.items())
    
    for pass_num in range(1, len(col)):
        swapped = False
        for i in range(len(col) - pass_num):
          
            if col[i][1] > col[i + 1][1]:
                col[i], col[i + 1] = col[i + 1], col[i]
                swapped = True
                
        if not swapped:
            break
            
    return dict(col)


sample_dict = {
    'elephant': 10,
    'cat': 2,
    'hippopotamus': 35,
    'dog': 4,
    'lion': 5
}

print(bubble_sort_dict_by_value(sample_dict))