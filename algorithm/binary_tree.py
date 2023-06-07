class MyNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def to_string(self):
        str_parent = "None"
        str_left = "None"
        str_right = "None"
        if self.parent != None:
            str_parent = str(self.parent.val)
        if self.left != None:
            str_left = str(self.left.val)
        if self.right != None:
            str_right = str(self.right.val)
        return "(" + str(self.val) + ", " + str_parent + ", " + str_left + "," + str_right + ")"

class MyBSTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        parent = None
        ptr = self.root
        while ptr != None:
            parent = ptr
            if node.val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right

        node.parent = parent
        if parent == None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            y = self.search_min(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def traverse(self, node):
        if node!= None:
            self.traverse(node.left)
            print(node.val, end=" ")
            self.traverse(node.right)

    def search(self, node, key):
        if node == None or node.val == key:
            return node
        elif key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
        return node

    def search_min(self, node):
        while node.left != None:
            node = node.left
        return node

if __name__ == "__main__":
    my_tree = MyBSTree()
    my_tree.insert(MyNode(13))
    my_tree.insert(MyNode(7))
    my_tree.insert(MyNode(10))
    my_tree.insert(MyNode(22))
    my_tree.insert(MyNode(16))
    my_tree.insert(MyNode(3))
    my_tree.insert(MyNode(15))
    my_tree.insert(MyNode(19))

    print("初期状態:")
    my_tree.traverse(my_tree.root)
    print("")

    x = my_tree.search(my_tree.root, 22)
    if x!= None:
        print("要素が見つかりました: x =", x.val)
    else:
        print("要素が見つかりませんでした。")

    if x!= None:
        my_tree.delete(x)
        print("要素の削除後:")
        my_tree.traverse(my_tree.root)
        print("")
    else:
        print("要素はNoneです。")
