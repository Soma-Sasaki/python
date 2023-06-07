import math

INFTY = 2**31 - 1

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

class MyHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_max_heap()

    def  max_heapify(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[index] < self.arr[left]:
            largest = left
        else:
            largest = index
        if right < self.size and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != index:
            swap(self.arr, index, largest)
            self.max_heapify(largest)

    def create_max_heap(self):
        self.size = len(self.arr)
        for i in range(math.floor(self.size / 2) - 1, -1, -1):
            self.max_heapify(i)

    def get_parent(self, index):
        return math.floor((index + 1) / 2) - 1

    def get_left(self, index):
        return 2 * (index + 1) - 1

    def get_right(self, index):
        return 2 * (index + 1)

    def extract_max(self):
        if self.size < 1:
            primt("ヒープは空です")
            return None
        max = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.arr.pop(self.size - 1)
        self.size -= 1
        self.max_heapify(0)
        return max

    def insert(self, val):
        self.size += 1
        self.arr.append(-INFTY)
        self.increase_val(self.size - 1, val)

    def increase_val(self, index, val):
        if self.arr[index] > val:
            print("値が増えていません。")
            return None
        self.arr[index] = val
        while index > 0 and self.arr[self.get_parent(index)] < self.arr[index]:
            swap(self.arr, index, self.get_parent(index))
            index = self.get_parent(index)

    def heap_sort(self):
        for i in range(self.size - 1, 0, -1):
            swap(self.arr, 0, i)
            self.size -= 1
            self.max_heapify(0)
        self.size = len(self.arr)

    def to_string(self):
        return str(self.arr[:self.size])

if __name__ == '__main__':
    arr = [6, 3, 18, 8, 1, 13]
    my_heap = MyHeap(arr)
    print("最大ヒープ化後のヒープ: ", my_heap.to_string())
    my_heap.insert(10)
    print(my_heap.to_string())
    my_heap.heap_sort()
    print(my_heap.to_string())
