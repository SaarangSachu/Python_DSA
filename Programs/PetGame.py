class Pet:
    def __init__(self,name):
        self.name=name
        self.hunger=0
        self.happiness=100
        self.energy=100

    def feed(self):
        self.hunger-=20
        if self.hunger<0:
            self.hunger=0

        self.energy-=10
        if self.energy>100:
            self.energy=100

        print(f"{self.name} ate a snack! Hunger is now {self.hunger}")

    def play(self):
        self.happiness+=20
        if self.happiness>100:
            self.happiness=100

        self.hunger+=15
        if self.hunger>=100:
            print("pet died")

        self.energy-=20
        if self.energy<=0:
            print("pet died")

    def sleep(self):
        self.energy=100
        self.hunger+=10
        print(f"{self.name} took a nap enrgy is {self.energy} Hunger is {self.hunger}")

    def pass_time(self):
        self.hunger+=10
        if self.hunger>=100:
            print("pet died")

        self.energy-=5
        if self.energy<=0:
            print("pet died")

        self.happiness-=10
        if self.happiness<=0:
            print("pet died")

    def show_status(self):
        print(f"--- {self.name}'s Status ---\nHunger: {self.hunger}/100\nHappiness: {self.happiness}/100\nEnergy: {self.energy}/100")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        super().play()
        self.happiness+=10
        if self.happiness>=100:
            self.happiness=100

class Cat(Pet):
    def __init__(self,name):
        super().__init__(name)

    def sleep(self):
        super().sleep()
        self.happiness+=20
        if self.happiness>=100:
            self.happiness=100


my_pet=Dog("jimmy")
while True:
    my_pet.show_status()
    if my_pet.hunger>=100 or my_pet.energy<=0 or my_pet.happiness<=0:
        print("pet died")
        break

    choice=int(input("what you want to do \n 1)Feed 2)Play 3)sleep 4)Exit\n"))
    match choice:
        case 1:
            my_pet.feed()
        case 2:
            my_pet.play()
        case 3:
            my_pet.sleep()
        case 4:
            decison=input("Are you sure (Y/N)\n")
            if decison.lower()=="y":
                break
            if decison.lower()=="n":
                continue
    my_pet.pass_time()