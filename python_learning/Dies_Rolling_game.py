import random

while True:
    choice=input("want to roll the dies.... (y/n)")
    if choice.lower()=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice.lower()=='n':
        print("Thank you for playing :) ")
        break
    else:
        print('invalid input')