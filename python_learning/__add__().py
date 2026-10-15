class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __add__(self,other):
        return self.age+other.age

p1=Person("rohan",12)
p2=Person("tom",34)
print(p1+p2)