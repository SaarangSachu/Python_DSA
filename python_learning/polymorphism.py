class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def move(self):
        print("move")

class Boat(Vehicle):
    def move(self):
        print("sail")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("Fly")

car1=Car("kia","sonet")
boat1=Boat("suzuki","X300")
plane1=Plane("AirIndia","t6x0")

for i in (car1,boat1,plane1):
    print(i.name,end=",")
    print(i.model)
    i.move()