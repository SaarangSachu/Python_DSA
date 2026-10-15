# The __len__() method controls what the built-in len() function returns for your object
# Without __len__(), calling len(c1) would raise a TypeError, since Python would not know what "length" means for a Company.
class Company:
    def __init__(self,employee):
        self.employee=employee

    def __len__(self):
        return len(self.employee)

e1=Company(["sachu","tom","jack"])
print(len(e1))