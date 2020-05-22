class Queue(object):
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
    
    def enqueue(self, value):
        self.in_stack.append(value)
    
    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is Empty.")
    
    def size(self):
        return len(self.in_stack)+len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is Empty.")
    
    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is Empty")
    
    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))

    def print_queue(self):
        # self.out_stack.reverse()-> reverse함수는 변수자체에 적용되기 때문에 함부로 사용하면 다 섞임
        stack = reversed(self.out_stack)
        print(list(stack))
        print(self.out_stack)




if __name__=="__main__":
    queue = Queue()
    print("큐가 비었나요?{0}".format(queue.isEmpty()))
    print("큐에 숫자 0~9를 추가합니다!")
    for i in range(0,10):
        queue.enqueue(i)
    print("큐 크기: {0}".format(queue.size()))
    print("peek:{0}".format(queue.peek()))
    # queue.print_queue()
    print("dequeue:{0}".format(queue.dequeue()))
    print("peek: {0}".format(queue.peek()))
    print("큐가 비었나요? {0}".format(queue.isEmpty()))
    print(queue)