N = int(input())
Floor = list(int(input()) for _ in range(N))

move = Floor[0] - 1

for i in range(N-1):
    move += abs(Floor[i] - Floor[i+1])

print(move)
    
