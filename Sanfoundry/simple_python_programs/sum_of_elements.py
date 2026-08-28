# find sum of the elements in a list using recursion
def sum_arr(col,size):
    if(size==0):
        return 0
    else:
        return col[size-1]+sum_arr(col,size-1)


col=[10,20,30]
size=len(col)

print(sum_arr(col,size))