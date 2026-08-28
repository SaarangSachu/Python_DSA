number=int(input("enter a number \t"))
temp=number
reverse=0
while temp>0:
    reverse=reverse*10+(temp%10)
    temp=temp//10

if number==reverse:
    print("the number is palindrome")
else:
    print("the number is not a palindrome")
