m, p, q = map(int, input().split())

P = p/100
Q = q/100

raw = m*P
sozai = (m-raw)*Q

print(m-raw-sozai)
