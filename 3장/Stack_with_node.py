class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, value):
        self.head = Node(value, self.head)
        self.count +=1
    
    def pop(self):
        if self.count>0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is Empty")
    
    def peek(self):
        if self.count >0 and self.head:
            return self.head.value
        else:
            print("Stack is Empty")

    def size(self):
        return self.count

    def print_List(self):
        node = self.head
        while node:
            print(node.value, end=",")
            node = node.pointer
        print()

if __name__=="__main__":
    stack = Stack()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(0,10):
        stack.push(i)
    print("스택 크기: {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack.print_List())