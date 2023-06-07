print("好きな数字を2つスペースを空けて入力してください")
A, B = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

ans=int(A*B/gcd(A,B))

print(f"入力した2数の最小公倍数は{ans}です")
