class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age

s1=Student("tom",12)
s2=Student("tom",12)
s3=Student("hom",12)

print(s1==s2==s3)