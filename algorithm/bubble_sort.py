def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def bubble_sort(arr, n):
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)

if __name__ == '__main__':
    arr = [3, 5, 1, 7, 2, 1]
    print("ソート前: ", arr)
    bubble_sort(arr, len(arr))
    print("ソート後: ", arr)
