class MyQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        if (self.tail + 1) % self.size == self.head:
            return None
        self.arr[self.tail] = val
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.head == self.tail:
            return None
        elm = self.arr[self.head]
        self.arr[self.head] = -1
        self.head = (self.head + 1) % self.size
        return elm

    def to_string(self):
        stringfied_data = "[ "
        index = self.head
        while index != self.tail:
            stringfied_data += str(self.arr[index]) + " "
            index = (index + 1) % self.size
        return stringfied_data + "]"

if __name__ == '__main__':
    a = MyQueue(10)
    for i in [1, 7, 3, 6, 9, 2, 4, 8, 5]:
        a.enqueue(i)
    a.to_string()
    for i in range(5):
        a.dequeue()
    a.to_string()
