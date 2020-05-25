class Queue(object):
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is Empty.")

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is Empty.")
    
    def __repr__(self):
        return repr(self.items)

class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)
    
    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is Empty")

from collections import deque
q = deque(["버피", "잰더", "윌로"])
q.append("자일스")
print(q.popleft())
print(q.pop())
q.appendleft("엔젤")
print(list(q))

p = deque(maxlen=4)
p.append("엔젤")
p.append("하트")
p.rotate(1)
p.rotate(-1)
print(p)