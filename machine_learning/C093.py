# X, Y = map(int, input().split())
# Bob = (int(X/100) + int(X/10) + X%10)%10
# Alice = (int(Y/100) + int(Y/10) + Y%10)%10
Bob = sum(list(map(int, str(X))))
Alice = sum(list(map(int, str(Y))))
if Bob > Alice:
    print("Bob")
elif Bob < Alice:
    print("Alice")
else:
    print("Draw")
