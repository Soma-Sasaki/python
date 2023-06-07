N, M = map(int, input().split())
for i in range(1, N + 1):
    a, b = map(int, input().split())
    score = a - 5 * b
    if max(score, 0) >= M:
        print(i)
