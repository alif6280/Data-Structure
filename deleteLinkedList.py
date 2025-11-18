class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")
    
def delSpecNode(head, NodeToDelete):
    if head == NodeToDelete:
        return head.next
        
    currentNode = head
    while currentNode.next and currentNode.next != NodeToDelete:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next
    return head

node1 = Node(5)
node2 = Node(10)
node3 = Node(2)
node4 = Node(15)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before Deletion : ")
traverseAndPrint(node1)

node1 = delSpecNode(node1, node3)
print("After Deletion : ")
traverseAndPrint(node1)
