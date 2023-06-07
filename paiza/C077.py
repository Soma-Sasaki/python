k,n=map(int,input().split())

for _ in range(k):
    d,a=map(int,input().split())
    score=int(a*100/n)
    if d>=10:
        score=0
    elif d>=1 and d<=9:
        score=int(score*0.8)

    if score>=80:
        print("A")
    elif score<=79 and score>=70:
        print("B")
    elif score<=69 and score>=60:
        print("C")
    elif score<=59:
        print("D")
