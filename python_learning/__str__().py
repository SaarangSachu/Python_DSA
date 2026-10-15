class Student:
    college="TVK"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"name of student is {self.name}")
        print(f"age of student is {self.age}")

    @classmethod
    def display(cls):
        print(f"college name is {cls.college}")

    @staticmethod
    def area():
        print(f"area is 100sq ft")

    def __str__(self):
        return f"the student name is {self.name}\nage is {self.age}\nhe is in {Student.college}"
s1=Student("tom",12)
print(s1)