arr=[[1,2,3],[3,4,5],[6,7,8]]

sum_of_diagoal=0
sum_of_anti_diagonal=0

for i in range(len(arr)):
    sum_of_diagoal+=arr[i][i]
    sum_of_anti_diagonal+=arr[i][len(arr)-1-i]

total=sum_of_anti_diagonal+sum_of_diagoal
print(total)
