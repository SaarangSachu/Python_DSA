class dnode:
    def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

class dll:
        def __init__(self):
            self.head=None
            self.tail=None

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
                current=current.next
                count+=1
            return count
             
              

        def insert_begining(self,data):
              new_node=dnode(data)
              if self.head==None:
                    new_node.next=self.head
                    self.head=new_node
                    self.tail=new_node
                    return
              new_node.next=self.head
              self.head.prev=new_node
              self.head=new_node

        def insert_end(self,data):
              new_node=dnode(data)
              if self.head==None:
                    new_node.next=self.head
                    self.head=new_node
                    self.tail=new_node
                    return
              new_node.prev=self.tail
              self.tail.next=new_node
              self.tail=new_node

        def insert_between(self,data,index):
             if 0<=index<=len(self):
                  if index==0:
                       return self.insert_begining(data)
                  elif index==len(self):
                       return self.insert_end(data)
                  else:
                       
                       new_node=dnode(data)
                       next_node=self[index]
                       prev_node=self[index-1]

                       prev_node.next=new_node
                       new_node.prev=prev_node

                       new_node.next=next_node
                       next_node.prev=new_node
             else:
                  print('index out of range')

        def delete_beginig(self):
             if self.head != None:
                  node=self.head
                  if self.head==self.tail:
                       self.head=None
                       self.tail=None
                       data=node.data
                       del node
                       return data
                  self.head=self.head.next
                  self.head.prev=None
                  data=node.data
                  del node
                  return data
             
        def delete_end(self):
             if self.head!=None:
                  node=self.tail
                  if self.head==self.tail:
                       self.head=None
                       self.tail=None
                       data=node.data
                       del node
                       return data
                  self.tail=self.tail.prev
                  self.tail.next=None
                  node.prev=None
                  data=node.data
                  del node
                  return data
             else:
                  print("list empty")

        def delete_between(self,index):
             if 0<=index<len(self):
                  if index==0:
                       return self.delete_beginig()
                  elif index==len(self)-1:
                       return self.delete_end()
                  else:
                       node=self[index]
                       next_node=self[index+1]
                       prev_node=self[index-1]

                       prev_node.next=next_node
                       next_node.prev=prev_node

                       node.next=None
                       node.prev=None
                       data=node.data
                       del node
                       return data
                  

        
        def display_front(self):
             current=self.head
             while current:
                  print(current.data)
                  current=current.next

        def display_end(self):
             current=self.tail
             while current:
                  print(current.data)
                  current=current.prev

        
                  
              
                    
d=dll()
d.insert_begining(20)
d.insert_begining(10)
d.insert_end(40)
d.insert_end(50)
d.insert_end(60)
d.insert_between(30,2)
d.display_front()      
print("")
d.display_end()  
print("")
d.delete_beginig()
d.delete_end()
d.delete_between(2)
d.display_front()