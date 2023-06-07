class MyElement:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, element):
        if self.tail == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element

    def dequeue(self):
        if self.head == None:
            return None
        elm = self.head
        self.head = elm.next
        if elm.next == None:
            self.tail = None
        elm.next = None
        return elm

    def to_string(self):
        stringfied_data = "[ "
        ptr = self.head
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next
        return stringfied_data + "]"

if __name__ == '__main__':
    a = MyQueue()
    for i in [1, 7, 3, 6, 9, 2, 4, 8, 5]:
        a.enqueue(MyElement(i))
    a.to_string()
    for i in range(5):
        a.dequeue()
    a.to_string()
