class Bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        if self.key>data:
            if self.lchild==None:
                self.lchild=Bst(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild==None:
                self.rchild=Bst(data)
            else:
                self.rchild.insert(data)

    def pre_order(self):
        if self.key==None:
            print("tree is empty")
            return
        print(self.key)
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()



r=Bst(10)
r.insert(20)
r.insert(5)
r.pre_order()