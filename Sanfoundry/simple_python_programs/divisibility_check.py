start=int(input("enter starting"))
end=int(input("enter ending"))
num=int(input("enter the number"))

for i in range(start,end+1):
    if(i%num==0):
        print(i)