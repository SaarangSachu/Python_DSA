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
    
    def inser_begining(self,data):
        new_node=snode(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=snode(data)
        if self.head == None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def insert_between(self,data,index):
        if 0<=index<=len(self):
            if index==0:
                self.inser_begining(data)
            elif index==len(self):
                self.insert_end(data)
            else:
                new_node=snode(data)
                prev=self[index-1]
                next=self[index]
                prev.next=new_node
                new_node.next=next

    def delete_begining(self):
        if self.head!=None:
            node=self.head
            self.head=self.head.next
            data=node.data
            del node
            return data
        else:
            print('no node is present')

    def delete_end(self):
        if self.head==None:
            print("no node is present")
        elif self.head.next==None:
            node=self.head
            data=node.data
            self.head=None
            del node
            return data
        else:
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
                next=node.next

                prev.next=next
                data=node.data
                del node
                return data
        else:
            print("invalid index")

    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        else:
            print("target not found")
            return False
            
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next


s=sll()
s.inser_begining(10)
s.inser_begining(20)
s.insert_end(30)
s.insert_between(23,0)

s.display()
print("")
print("deleted ",s.delete_begining())
s.display()
print('deleted ',s.delete_end())
s.display()
print('deleted ',s.delete_between(1))
s.display()
print(s.search(20))
