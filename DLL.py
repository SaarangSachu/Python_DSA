class dnode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_begining(self,data):
        new_node=dnode(data)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
            self.tail=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


    