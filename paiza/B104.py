import numpy as np
N, M = map(int, input().split(" "))
l = [list(input().split(" ")) for l in range(N)]
sum = np.zeros(M)
count = np.zeros(M)
for i in range(N):
    for j in range(M):
        if (l[i][j].isdigit()):
            if (int(l[i][j])>=0) & (int(l[i][j])<=100):
                l[i][j] = int(l[i][j])
                sum[j] += l[i][j]
                count[j] += 1
            else:
                l[i][j] = None
        else:
            l[i][j] = None

average = sum / count

for i in range(M):
    print(int(average[i]))
