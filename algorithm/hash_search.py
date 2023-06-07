class MyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def to_string(self):
        return "(" + str(self.key) + ", " + str(self.val) + ")"

class MyHashTable:
    def __init__(self, size):
        self.tbl = [None] * size

    def __get_hash(self, key):
        return key % len(self.tbl)

    def insert(self, key, val):
        hash_val = self.__get_hash(key)
        n = MyNode(key, val)
        if self.tbl[hash_val] == None:
            self.tbl[hash_val] = n
        else:
            ptr = self.tbl[hash_val]
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = n

    def delete(self, key):
        hash_val = self.__get_hash(key)
        prev_ptr = None
        ptr = self.tbl[hash_val]
        while ptr != None:
            if ptr.key == key:
                if ptr.next != None:
                    if prev_ptr != None:
                        prev_ptr.next = ptr.next
                    else:
                        self.tbl[hash_val] = ptr.next
                else:
                    if prev_ptr != None:
                        prev_ptr.next = None
                    else:
                        self.tbl[hash_val] = None
                return None
            prev_ptr = ptr
            ptr = ptr.next

    def search(self, key):
        hash_val = self.__get_hash(key)
        if self.tbl[hash_val] != None:
            ptr = self.tbl[hash_val]
            if ptr.key == key:
                return ptr
            while ptr.next != None:
                ptr = ptr.next
                if ptr.key == key:
                    return ptr
        return None

    def to_string(self):
        stringfied_tbl = ""
        for i in range(0, len(self.tbl)):
            if self.tbl[i] != None:
                stringfied_tbl += "tbl[" + str(i) + "] ->" + self.tbl[i].to_string()
                ptr = self.tbl[i]
                while ptr.next != None:
                    ptr = ptr.next
                    stringfied_tbl += "->" + ptr.to_string()
                stringfied_tbl += "\n"
        return stringfied_tbl

if __name__ == '__main__':
    my_hash = MyHashTable(10)

    for i, j in zip([3, 12, 233, 95, 183, 25], ["Alice", "Bob", "Chris", "David", "Eav", "George"]):
        my_hash.insert(i, j)
    print(my_hash.to_string())
    x = my_hash.search(233)
    if x != None:
        print("取得した要素", x.to_string())
    else:
        print("指定したキーに対応する要素が存在しません。")
    my_hash.delete(233)
    print(my_hash.to_string())
