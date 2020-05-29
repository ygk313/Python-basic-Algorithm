import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue=[]
        self._index=0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index +=1
    
    def pop(self):
        return heapq.pop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return repr(self.name)


def test_priority_queue():
    q = PriorityQueue()
