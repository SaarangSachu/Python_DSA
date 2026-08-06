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
        
        if self.key>data:
            if self.lchild==None:
                self.lchild=bst(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild==None:
                self.rchild=bst(data)
            else:
                self.rchild.insert(data)
        
        
    def inorder(self):
        if self.key==None:
            print("tree is empty")
        else:
            if self.lchild:
                self.lchild.inorder()
            print(self.key,end=' ')
            if self.rchild:
                self.rchild.inorder()

    def postorder(self):
        if self.key==None:
            print('tree is empty')
            return
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')

    def preporder(self):
        if self.key==None:
            print("tree is empty")
            return
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preporder()
        if self.rchild:
            self.rchild.preporder()

    def bfs(self):
        if self.key==None:
            print("tree is empty")
            return
        queue=[self]
        while queue:
            current=queue.pop(0)
            print(current.key,end=" ")

            if current.lchild:
                queue.append(current.lchild)
            if current.rchild:
                queue.append(current.rchild)

    def search(self,data):
        if self.key==None:
            print("tree is empty")
            return
        if self.key==data:
            print("node is present")
            return
        elif self.key>data:
            if self.lchild==None:
                print("node not present")
                return
            else:
                self.lchild.search(data)
        else:
            if self.rchild==None:
                print("node is not present")
                return
            else:
                self.rchild.search(data)

    def min_node(self):
        if self.key==None:
            print("the tree is empty")
            return
        node=self
        while node.lchild:
            node=node.lchild
        print(node.key)

    def max_node(self):
        if self.key==None:
            print("the tree is empty")
            return
        node=self
        while node.rchild:
            node=node.rchild
        print(node.key)
        
root=bst(None)
root.inorder()
l=[10,5,12,3,6,11,16]
for i in range(len(l)):
    root.insert(l[i])
root.inorder()
print("")
root.postorder()
print("")
root.preporder()
print("")
root.bfs()
print("")
root.search(2)

root.min_node()

root.max_node()