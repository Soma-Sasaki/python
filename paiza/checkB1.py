n, m = map(int, input().split())
seats = [True] * n
for i in range(m):
    a, b = map(int, input().split())
    if all(seats[seat % n] for seat in range(b - 1, a + b - 1)):
        for j in range(b - 1, a + b - 1):
            seats[j % n] = False

print(seats.count(False))
