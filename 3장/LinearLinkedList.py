class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value
    
    def getNext(self):
        return self.pointer

    def setData(self, value):
        self.value = value
    
    def setPointer(self, pointer):
        self.pointer = pointer

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length =0

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
    
    def _add(self, value):
        self.head = Node(value,self.head)
        self.length += 1
    
    def _find(self, index):
        prev = None
        node = self.head
        i=0
        while node and i<index:
            prev = node
            node = node.pointer
            i += 1
        return prev, node, i
    
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer
    
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False

        while node and not found:
            if value == node.value:
                found = True
            else:
                prev = node
                node = node.pointer
        
        return node, prev, found

    # 인덱스로 지우기
    def deleteNode(self, index):
        prev, node, i = self._find(index)
        if i==index:
            self._delete(prev, node)
        else:
            print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    # 값으로 지우기
    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)

        if found:
            self._delete(prev, node)
        else:
            print(f"해당 값 {value}에 해당하는 노드가 없습니다.")

class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
    
    def _addFirst(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def _deleteFirst(self):
        self.head = None
        self.tail = None
        self.length = 0
        print("연결리스트가 비었습니다.")
    
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node
    
    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)
    
    def _find(self, index):
        i=0
        prev = None
        node = self.head

        while node and i<index:
            prev = node
            node = node.pointer
            i+=1
        
        return prev, node, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False

        while not found and node:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        
        return prev, node, found

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            prev, node, i = self._find(index)
            if i==index and node:
                self.length -= 1
                if i==0 or not prev:
                    self.head = node.pointer
                    # self.tail = node.pointer
                    print(self.tail.value, self.head.value)
                else:
                    prev.pointer = node.pointer
            else:
                print("인덱스에 해당하는 노드가 없습니다.")

    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            prev, node, found = self._find_by_value(value)        
            if node and found is True:
                self.length -= 1
                if not prev :
                    self.head = node.pointer
                    # self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("찾는 값이 없습니다.")


if __name__=="__main__":
    li = LinkedListFIFO()
    for i in range(1,5):
        li.addNode(i)
    print("연결리스트 출력:")
    li._printList()
    print("인덱스가 2인 노드 삭제후, 연결리스트 출력:")
    li.deleteNode(2)
    li._printList()
    print("값이 15인 노드 추가 후, 연결리스트 출력:")
    li._add(15)
    li._printList()
    print("인덱스가 0인 노드 삭제후, 연결리스트 출력:")
    li.deleteNode(0)
    li._printList()
    print("값이 15인 노드 추가 후, 연결리스트 출력:")
    li._add(15)
    li._printList()
    print("모든 노드 모두 삭제 후, 연결리스트 출력:")
    for i in range(li.length-1, -1, -1):
        li.deleteNode(i)
    li._printList()