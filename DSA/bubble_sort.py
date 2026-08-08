def bubble_sort(col):
    for pass_num in range(1,len(col)):
        for i in range(len(col)-pass_num):
            if col[i]>col[i+1]:
                col[i],col[i+1]=col[i+1],col[i]
    
    return col

print(bubble_sort([7,30,10,50,45,63,1]))
