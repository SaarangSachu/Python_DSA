list1=[1,3,4,5]
list2=[2,4,7]
sorted_list=[]
i=j=0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        sorted_list.append(list1[i])
        i+=1
    else:
        sorted_list.append(list2[j])
        j+=1

if i<len(list1):
    sorted_list.extend(list1[i:])
if j<len(list2):
    sorted_list.extend(list2[j:])

print(sorted_list) 