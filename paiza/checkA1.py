num, finger = map(int,input().split())
hands = input()
g = hands.count("G")
c = hands.count("C")
p = num - g - c
max_win = 0

for i in range((finger//5) + 1):
    for j in range(num + 1 - i):
        if 5*i + 2*j == finger:
            max_win = max(max_win, min(g, i) + min(p, j) + min(c, num - i - j))

print(max_win)
