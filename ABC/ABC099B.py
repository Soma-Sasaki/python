a, b = map(int, input().split())
sub = b - a
B = (1 / 2) * sub * (sub + 1)
print(int(B - b))
