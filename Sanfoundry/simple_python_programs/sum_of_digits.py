sum=0

def sum_of_digit(num):
    global sum
    if num==0:
        return sum
    
    sum=sum+(num%10)
    return sum_of_digit(num//10)

print(sum_of_digit(1234))
    