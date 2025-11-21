class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.data = x
        
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)
        
def printPreorder(root):
    if root:
        print(root.data,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data,end=" ")
        
if __name__ == "__main__":
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)
print("Inorder Traversal : ",end=" ")
printInorder(root)
print("\nPreorder Traversal : ",end=" ")
printPreorder(root)
print("\nPostorder Traversal : ",end=" ")
printPostorder(root)
