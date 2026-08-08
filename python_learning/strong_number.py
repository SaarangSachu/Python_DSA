# strong number are numbers whose sum of factorail of digits == digit
# 145
# # 1 fact=1
# 4 fact = 24
# 5 fact = 120
# sum = 1+24+120=145
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

def strong_number(num):
    sum=0
    for i in str(num):
        sum=sum+fact(int(i))
    if sum==num:
        return True
    else :
        return False
    
print(strong_number(145))

