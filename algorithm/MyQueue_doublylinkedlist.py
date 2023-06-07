import os
os.chdir(r"C:\Users\shira\Desktop\python\algorithm")
import MyDoublyLinkedList

class MyQueue:
    def __init__(self):
        self.dlist = MyDoublyLinkedList.MyDoublyLinkedList()

    def enqueue(self, element):
        self.dlist.append(element)

    def dequeue(self):
        elm = self.dlist.get(0)
        self.dlist.delete(elm)
        return elm

    def to_string(self):
        return self.dlist.to_string()

if __name__ == '__main__':
    a = MyQueue()
    for i in [1, 7, 3, 6, 9, 2, 4, 8, 5]:
        a.enqueue(MyDoublyLinkedList.MyElement(i))
    a.to_string()
    for i in range(5):
        a.dequeue()
    a.to_string()
