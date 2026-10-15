class Student:
    def __init__(self,name):
        self.name=name

    def __contains__(self, item):
        return item in self.name

s1=["tom","don","ron","mon"]
print("tom" in s1)