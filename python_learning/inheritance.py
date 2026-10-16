class Person:
    college="TVK"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name : {self.name}\nage : {self.age}\ncollege : {Person.college}")

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.graduation=2030

    def greetings(self):
        print(f"ThankYou {self.name} for joining {self.college} \nyou will graduate on {self.graduation}\n")


s=Student("tom",34)
s.display()
s.greetings()