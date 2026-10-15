# The __call__() method lets an object be called like a function, using object() syntax.
class Counter:
    def __init__(self):
        self.counter=0

    def __call__(self):
        self.counter+=1
        return self.counter

button=Counter()
print(button())
print(button())
print(button())