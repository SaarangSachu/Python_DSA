class snode:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def __getitem__(self, index):
        count=0
        current=self.head
        while count<index:
            current=current.next
            count+=1
        return current

    def __len__(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count


    def insert_begining(self,data):
        new_node=snode(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=snode(data)
        if self.head==None:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def indert_between(self,data,index):
        if 0<= index <= len(self):
            if index==0:
                return self.insert_begining(data)
            elif index==len(self):
                return self.insert_end(data)
            else:
                new_node=snode(data)
                prev=self[index-1]
                next=self[index]

                prev.next=new_node
                new_node.next=next
        else:
            print("index is out of range")

    def delete_begining(self):
        if self.head==None:
            print("empty")
            return
        node=self.head
        self.head=self.head.next
        data=node.data
        del node
        return data

    def delete_end(self):
        if self.head==None:
            print("empty")
            return
        prev=self[len(self)-2]
        node=self[len(self)-1]

        prev.next=None
        data=node.data
        del node
        return data

    def delete_between(self,index):
        if 0<=index<len(self):
            if index==0:
                return self.delete_begining()
            elif index==len(self)-1:
                return self.delete_end()
            else:
                prev=self[index-1]
                node=self[index]
                next=self[index+1]

                prev.next=next
                data=node.data
                del node
                return data        
        

    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

s=sll()
s.insert_begining(10)
s.insert_end(30)
s.insert_end(30)
s.insert_end(30)
s.indert_between(20,1)
s.display()
print("")
print(s.delete_end())
s.display()
print("")
print(s.delete_begining())
s.display()
print("")
print(s.delete_between(1))
print("")
s.display()
