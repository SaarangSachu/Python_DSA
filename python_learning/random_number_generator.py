import random
while True:
    choice=input("generate..? (y/n)")
    if choice.lower()=='y':
        start=int(input("start from .... "))
        end=int(input("end till .... "))
        print(f"your randum number is ({random.randint(start,end)})")
    elif choice.lower=='n':
        print("bye bye")
    else:
        print("invalid input")