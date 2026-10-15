class Studenet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f"Student('{self.name}',{self.age})"

    def __str__(self):
        return f"name of student is {self.name}\nAge is {self.age}\n"

s1=Studenet("Rohan",56)
print(s1)
print(repr(s1))