N, X = map(int, input().split())

fare = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    n = (X - a) / c

    if n >= 0 :
        fare.append(b + (int(n)+1)*d)
    else:
        fare.append(b)

print(min(fare), max(fare))
