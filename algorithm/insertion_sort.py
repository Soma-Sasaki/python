def insertion_sort(arr, n):
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

if __name__ == '__main__':
    arr = [3, 5, 1, 7, 2, 1]
    print("ソート前: ", arr)
    insertion_sort(arr, len(arr))
    print("ソート後: ", arr)
