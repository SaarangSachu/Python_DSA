class stack:
    def __init__(self):
        self.stack=[]
    def push_item(self,data):
        self.stack.append(data)
        print(data,' pushed to stack')
    def pop_item(self):
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
s.push_item(2)
s.push_item(15)
s.push_item(30)
print(s.stack)
s.pop_item()
print(s.stack)
s.pop_item()
s.pop_item()
print(s.is_empty())

a=stack()
a.push_item(12)
a.push_item(22)
print(a.stack)