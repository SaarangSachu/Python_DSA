import random
answer=random.randint(1,100)

while True:
    choice=int(input("guess the number between 1 and 100  \n"))
    if choice<answer:
        print("too low")
    elif choice>answer:
        print("too high")
    elif choice==answer:
        print("congratulations")
        break
    else:
        print("invalid choice")