def bubble_sort_dict_by_key_length(my_dict):
    col = list(my_dict.items())
    
    for pass_num in range(1, len(col)):
        swapped = False
        for i in range(len(col) - pass_num):

            if len(col[i][0]) > len(col[i + 1][0]):
                col[i], col[i + 1] = col[i + 1], col[i]
                swapped = True
        if not swapped:
            break
        print("after ",pass_num," th pass",col)  
    
    return dict(col)


sample_dict = {
    'elephant': 1,
    'cat': 2,
    'cow': 3,
    'dog': 4,
    'lion': 5
}

print(bubble_sort_dict_by_key_length(sample_dict))