col, row = map(int, input().split())
map_list = [["0"] * (col+2)]
for i in range(row):
    map_list.append(["0"] + input().split() + ["0"])
map_list.append(map_list[0])

def check(x, y):
    lands = [[x, y]]
    while lands:
        x, y = lands.pop()
        map_list[x][y] = "0"
        # 下の場所
        if map_list[x][y+1] == "1":
            lands.append([x, y+1])
        # 右の場所
        if map_list[x+1][y] == "1":
            lands.append([x+1, y])
        # 上の場所
        if map_list[x][y-1] == "1":
            lands.append([x, y-1])
        # 左の場所
        if map_list[x-1][y] == "1":
            lands.append([x-1, y])

count = 0
for i in range(1, row+1):
    for j in range(1, col+1):
        if map_list[i][j] == "1":
            check(i, j)
            count += 1

print(count)
