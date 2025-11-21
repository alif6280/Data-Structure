class Stack:
    def __init__(self):
        self.x = []

    def push(self, value):
        self.x.append(value)

    def pop(self):
        if len(self.x) > 0:
            self.x.pop()
        else:
            print("Stack is empty")

    def top(self):
        if len(self.x) > 0:
            print("Top Element :", self.x[-1])
        else:
            print("Stack is empty")

    def empty(self):
        return len(self.x) == 0

    def size(self):
        return len(self.x)

    def insert(self, index, value):
        if index < 0 or index > len(self.x):
            print("Invalid Index")
            return
        self.x.insert(index, value)
        print("Inserted.....!")

    def deleteat(self, index):
        if index < 0 or index >= len(self.x):
            print("Invalid Index.")
            return
        self.x.pop(index)
        print("Deleted...!")

    def show(self):
        if len(self.x) == 0:
            print("Stack is empty")
            return
        print("Stack Element :", *self.x)


# Main Program
s = Stack()

while True:
    print("\n-----MENU-----")
    print("1. Push")
    print("2. Pop")
    print("3. Top Show")
    print("4. Insert Element")
    print("5. Delete Element")
    print("6. Show All Element")
    print("7. Size Element")
    print("8. Exit")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        value = int(input("Enter Value : "))
        s.push(value)

    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.top()

    elif ch == 4:
        index = int(input("Enter Index : "))
        value = int(input("Enter Value : "))
        s.insert(index, value)

    elif ch == 5:
        index = int(input("Enter Index : "))
        s.deleteat(index)

    elif ch == 6:
        s.show()

    elif ch == 7:
        print("Element Size :", s.size())

    elif ch == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
