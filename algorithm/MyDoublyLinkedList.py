class MyElement:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def to_string(self):
        str_prev = "None"
        str_next = "None"
        if self.prev != None:
            str_prev = str(self.prev.val)
        if self.prev != None:
            str_next = str(self.next.val)
        return "(" + str(self.val) + "," + str_prev + "," + str_next + ")"



class MyDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.prev = self.tail
            self.tail = element

    def get(self, index):
        ptr = self.head
        for i in range(0, index):
            ptr = ptr.next
        return ptr

    def insert(self, index, element):
        ptr = self.get(index)
        if ptr == None:
            self.append(element)
        else:
            element.prev = ptr.prev
            element.next = ptr
            if ptr.prev == None:
                self.head = element
            else:
                ptr.prev.next = element
            ptr.prev = element

    def delete(self, element):
        if element.prev == None:
            self.head = element.next
        else:
            element.prev.next = element.next
        if element.next == None:
            self.tail = element.prev
        else:
            element.next.prev = element.prev

    def to_string(self):
        stringfied_data = "[ "
        ptr = self.head
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next
        return stringfied_data + "]"

if __name__ == "__main__":
    a = MyDoublyLinkedList()
    a.append(MyElement("A"))
    a.append(MyElement("B"))
    a.append(MyElement("C"))
    a.to_string()
