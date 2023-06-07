class MyElement:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, element):
        if not self.is_empty():
            element.next = self.top
        self.top = element

    def pop(self):
        if self.is_empty():
            return None
        elm = self.top
        self.top = elm.next
        elm.next = None
        return elm

    def to_string(self):
        stringfied_data = "[ "
        ptr = self.top
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next
        return stringfied_data + "]"

if __name__ == '__main__':
    a = MyStack()
    for i in [1, 7, 3, 6, 9, 2, 4, 8, 5]:
        a.push(MyElement(i))
    a.to_string()
    for i in range(5):
        a.pop()
    a.to_string()
    a.push(MyElement(10))
    a.to_string()
