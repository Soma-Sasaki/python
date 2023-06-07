n = int(input())
cards = [int(input())%7 for i in range(n)]
total = 0
for n1 in range(7):
    for n2 in range(7):
        for n3 in range(7):
            if (n1 + n2 + n3) %7 == 0:
                c1 = cards.count(n1)
                c2 = cards.count(n2)
                c3 = cards.count(n3)
                if n2 == n1:
                    c2 -= 1
                if n3 == n1:
                    c3 -= 1
                if n3 == n2:
                    c3 -= 1
                pat = c1*c2*c3
                total += pat
print(total//6)
