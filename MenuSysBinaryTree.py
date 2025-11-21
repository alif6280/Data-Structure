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

    while True:
        print("\n--- Menu ---")
        print("1. Inorder Traversal")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")
        print("4. Exit")
        
        ch = input("Enter choice : ")

        if ch == "1":
            print("Inorder Traversal : ", end=" ")
            printInorder(root)
            print()
        elif ch == "2":
            print("Preorder Traversal : ", end=" ")
            printPreorder(root)
            print()
        elif ch == "3":
            print("Postorder Traversal : ", end=" ")
            printPostorder(root)
            print()
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
