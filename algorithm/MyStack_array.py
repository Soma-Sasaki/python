class MyStack:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, val):
        if self.top == self.size - 1:
            return None
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.is_empty():
            return None
        elm = self.arr[self.top]
        self.arr[self.top] = -1
        self.top -= 1
        return elm

    def to_string(self):
        stringfied_data = "[ "
        for i in range(0, self.top + 1):
            stringfied_data += str(self.arr[i]) + " "
        return stringfied_data + "]"

if __name__ == '__main__':
    a = MyStack(10)
    for i in [1, 7, 3, 6, 9, 2, 4, 8, 5]:
        a.push(i)
    a.to_string()
    for i in range(5):
        a.pop()
    a.to_string()
