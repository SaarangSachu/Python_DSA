class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        if self.key==data:
            return
        elif self.key>data:
            if self.lchild==None:
                self.lchild=bst(data)
            else:
                self.lchild.insert(data)

        else:
            if self.rchild==None:
                self.rchild=bst(data)
            else:
                self.rchild.insert(data)
    def search(self,data):
        if self.key is None:
            print("empty")
            return
        if self.key==data:
            print("node is present")
            return
        elif self.key>data:
            if self.lchild is None:
                print("not present")
            else:
                self.lchild.search(data)
        else:
            if self.rchild is None:
                print("not present")
            else:
                self.rchild.search(data)
# root=bst(None)
# root.insert(10)
# root.insert(20)
# root.insert(5)
# root.insert(15)
root=bst(None)
l=[10,5,20,15,100]
for i in l:
    root.insert(i)

root.search(18)
# l=[10,5,20,15,100]
# root=bst(10)
# root.lchild=bst(5)
# root.rchild=bst(20)
# root.rchild.lchild=bst(15)
# root.rchild.rchild=bst(100)

print(root.key)
print(root.lchild.key)
print(root.rchild.key)
# print(root.rchild.rchild.key)
# print(root.rchild.lchild.key)