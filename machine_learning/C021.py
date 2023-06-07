xc, yc, r1, r2 = map(int, input().split())
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    d = (x-xc)**2 + (y-yc)**2
    if r1**2 <= d and d <= r2**2:
        print("yes")
    else:
        print("no")

xc, yc, r1, r2 = map(int, input().split())
n = int(input())
x = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    d = (x[i][0]-xc)**2 + (x[i][1]-yc)**2
    if r1**2 <= d and d <= r2**2:
        print("yes")
    else:
        print("no")
