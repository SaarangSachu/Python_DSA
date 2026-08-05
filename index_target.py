l=[3,4,2,8,7,1]
target=9


pairs=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            pairs.append((i,j))

print(pairs)