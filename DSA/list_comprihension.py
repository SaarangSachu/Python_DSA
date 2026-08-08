'''
list comprihension 
syntax
list=[
 [output expression]
 interation expression
 conditon expression
]
'''
x=3
y=3
z=3
n=11
list=[
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
   
    if i+j+k!=n
]

print(list)