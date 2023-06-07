print("好きな数字を2つスペースを空けて入力してください")
A, B = map(int, input().split())


if A < B:
    B, A = A, B


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(f"入力した2数の最大公約数は{gcd(A,B)}です")
