class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=tree(10)
root.left=tree(20)
root.right=tree(30)
root.left.left=tree(40)
root.left.right=tree(50)
root.right.left=tree(60)
root.right.right=tree(70)

print(root.data)
print(root.left.data)
print(root.right.data)

