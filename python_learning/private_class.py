class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0

    def set_grade(self,grade):
        if grade>=0 and grade<=100:
            self.__grade=grade
            print(f"{self.__grade} is accepted as vallid\n")
        else:
            print("enter a valid grade\n")

    def get_grade(self):
        print(self.__grade) 

    def get_statud(self):
        if self.__grade>35:
            print(f"{self.name} Passed\n")
        else:
            print(f"{self.name} Fail\n")

s1=Student("tom")
s1.set_grade(23)
s1.get_statud()
s1.set_grade(88)
s1.get_statud()