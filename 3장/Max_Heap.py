class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max__heapify(i)
    
    def __repr__(self):
        return self.data
    
    def parent(self, i):
        if i&1:
            return i>>1
        else:
            return (i>>1)-1
    
    def left_child(self,i):
        return (i<<1)+1
    
    def right_child(self, i):
        return (i<<1)+2
    
    def __max__heapify(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        largest = (left < n and self.data[i] <self.data[left]) and left or i
        largest = (right < n and self.data[largest] < self.data[right]) and right or largest

        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max__heapify(largest)
    
    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]
        self.data[0] = self.data[n-1]
        self.data = self.data[:n-1]
        self.__max__heapify(0)
        return max_element
    
    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i!=0) and item > self.data[0]:
            self.data[i] = self.data[self.paretn(i)]
            i = self.parent(i)
        self.data[i] =item


def test_heapify():
    l1 = [3,2,5,1,7,8,2]
    h= Heapify(l1)
    assert(h.extract_max()==8)
    print("테스트 통과")


if __name__=="__main__":
    test_heapify()
