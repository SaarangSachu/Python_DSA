class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
        print(data,' pushed to stack')
    def dequeue(self):
        if len(self.queue)!=0:
            return self.queue.pop(0)
        else:
            print("stack is empty")
    def last_element(self):
        if len(self.queue)!=0:
                    return self.queue[-1]
        else:
            print("stack is empty")
    def first_elemnt(self):
            if len(self.queue)!=0:
                        return self.queue[0]
            else:
                print("stack is empty")

    def is_empty(self):
         return len(self.queue)==0

s=queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
print(s.queue)
s.dequeue()
print(s.queue)
print(s.last_element())
print(s.first_elemnt())
print(s.is_empty())