class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return self.age<other.age

s1=Student("ram",12)
s2=Student("don",123)
s3=Student("ron",45)

x=sorted([s1,s2,s3])

print(x[0].name)
print(x[0].age)