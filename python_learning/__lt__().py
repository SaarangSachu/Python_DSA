# The __lt__() method ("less than") controls what the < operator does for your own objects.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return self.age<other.age

s1=Student("rahul",21)
s2=Student("tom",2)
print(s1<s2)