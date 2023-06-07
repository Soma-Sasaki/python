N, c1, c2 = map(int, input().split())
stock = list(int(input()) for _ in range(N))

benefit = 0
count = 0

for i in range(N-1):
    if c1 < stock[i]  and c2 > stock[i]:
        continue
    elif c1 >= stock[i]:
        benefit -= stock[i]
        count += 1
    else:
        benefit += stock[i]*count
        count = 0

print(benefit+stock[N-1]*count)
