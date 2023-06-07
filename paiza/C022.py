n = int(input())
S = [list(map(int, input().split())) for i in range(n)]

stock = []
stock.append(S[0][0])
stock.append(S[n-1][1])
stock.append(max([row[2] for row in S]))
stock.append(min([row[3] for row in S]))

print(*stock)
