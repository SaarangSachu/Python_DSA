class dnode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_beginig(self,data):
        new_node=dnode(data)
        if self.head==None:
            new_node.next=self.head
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_end(self,data):
        new_node=dnode(data)
        if self.head==None:
            new_node.next=self.head
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node