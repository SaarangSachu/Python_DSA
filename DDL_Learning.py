class dnode:
    def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

class dll:
        def __init__(self):
            self.head=None
            self.tail=None

        def insert_begining(self,data):
              if self.head==self.tail:
                