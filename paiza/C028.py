N = int(input())
QA = list(input().split() for _ in range(N))

score = 0


for i in range(N):
    if len(QA[i][0]) != len(QA[i][1]):
        continue

    penalty = 0
    for c1, c2 in zip(QA[i][0], QA[i][1]):
        if c1 != c2:
            penalty += 1

    if penalty >= 2:
        continue
    elif penalty == 1:
        score += 1
    else:
        score += 2


print(score)
