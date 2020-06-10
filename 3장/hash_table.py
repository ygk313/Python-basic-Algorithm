from LinearLinkedList import LinkedListFIFO

class Hashtable(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHasTable()
    
    def _createHasTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())
    
    def _find(self, item):
        return item%self.size
    
    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)
    
    def _delete(self,item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)
    
    def _print(self):
        for i in range(self.size):
            print("슬롯(slot) {0}:".format(i))
            self.slots[i]._printList()

H1 = Hashtable(3)
for i in range(0, 20):
    H1._add(i)
H1._print()
print("\n항목 0,1,2를 삭제합니다.")
H1._delete(0)
H1._delete(1)
H1._delete(2)
H1._print()