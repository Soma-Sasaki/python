def linear_search(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return None

if __name__ == '__main__':
    arr = [5, 1, 33, 25, 85, 12, 3, 8, 54, 17]
    print("配列: ", arr)

    index = linear_search(arr, 3)
    if index != None:
        print("arr[", index, "]に要素が見つかりました。")
    else:
        print("指定した数値は配列内に存在しません。")
