import math, os
os.chdir(r"C:\Users\shira\Desktop\python\algorithm")
import quick_sort

def binary_search(arr, key, p, r):
    if r < p:
        return None
    else:
        q = math.floor((r + p) / 2)
        if arr[q] < key:
            return binary_search(arr, key, q + 1, r)
        elif arr[q] > key:
            return binary_search(arr, key, p, q - 1)
        else:
            return q

if __name__ == '__main__':
    arr = [5, 1, 33, 25, 85, 12, 3, 8, 54, 17]
    quick_sort.quick_sort(arr, 0, len(arr) - 1)
    print("ソート済配列: ", arr)
    index = binary_search(arr, 8, 0, len(arr) - 1)
    if index != None:
        print("arr[", index, "]に要素が見つかりました。")
    else:
        print("指定した数値は配列内に存在しません。")
