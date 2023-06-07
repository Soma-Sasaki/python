H, W, X = map(int, input().split())

letter = ""
for _ in range(H):
    s = input()
    letter += s

for i in range(0,len(letter),X):
    print(letter[i:i+X])
