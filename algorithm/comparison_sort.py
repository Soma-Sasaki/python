import random, time, copy, os
os.chdir(r"C:\Users\shira\Desktop\python\algorithm")
import insertion_sort, bubble_sort, merge_sort, quick_sort

if __name__ == '__main__':
    arr = []
    N = 50000
    for i in range(0, N):
        arr.append(random.uniform(0, 1000000))

    start = time.time()
    insertion_sort.insertion_sort(copy.copy(arr), N)
    end = time.time()
    print("挿入ソートの処理時間 = ", end - start)

    start = time.time()
    bubble_sort.bubble_sort(copy.copy(arr), N)
    end = time.time()
    print("バブルソートの処理時間 = ", end - start)

    start = time.time()
    merge_sort.merge_sort(copy.copy(arr), 0, N - 1)
    end = time.time()
    print("マージソートの処理時間 = ", end - start)

    start = time.time()
    quick_sort.quick_sort(copy.copy(arr), 0, N - 1)
    end = time.time()
    print("クイックソートの処理時間 = ", end - start)
