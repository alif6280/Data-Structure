from collections import deque

q = deque()

q.append(100)
q.append(200)
q.append(300)
q.append(400)
q.append(500)

print("Queue Contents:", q)

removed = q.pop()
print("Dequeued :", removed)

print("After dequeue :", q)
