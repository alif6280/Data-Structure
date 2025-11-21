queue = []

while True:
    print("\n1.Enqueue")  
    print("2.Dequeue")
    print("3.Show")
    print("4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        value=input("Value : ")
        queue.append(value)
        print(f"{value} Enqueued.")
    elif ch == "2":
        if queue:
            value = input("Enter value to dequeue: ")
            if value in queue:
                queue.remove(value)
                print(f"{value} Dequeued.")
            else:
                print("Value not found in queue!")
        else:
            print("Queue Empty")
    elif ch == "3":
        print("Queue:",queue)
    elif ch == "4":
        break
    else:
        print("Invalid choice")
