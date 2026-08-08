class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
        print(data,' pushed to stack')
    def pop(self):
        if len(self.stack)!=0:
            return self.stack.pop()
        else:
            print("stack is empty")
    def peek(self):
        if len(self.stack)!=0:
                    return self.stack[-1]
        else:
            print("stack is empty")

    def is_empty(self):
         return len(self.stack)==0


s=stack()
s.push(2)
s.push(15)
s.push(30)
print(s.stack)
s.pop()
print(s.stack)
s.pop()
s.pop()
print(s.is_empty())

a=stack()
a.push(12)
a.push(22)
print(a.stack)