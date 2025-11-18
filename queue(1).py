from collections import deque

if __name__ == "__main__":
    q = deque()
    q.append(100)
    q.append(200)
    q.append(300)
    q.append(400)
    q.append(500)
    print("Queue contents:", q)
    #deque
    element = q.pop()
    print(element)
    element = q.pop()
    print(element)
    element = q.pop()
    print(element)
    element = q.pop()
    print(element)
    element = q.pop()
    print(element)
