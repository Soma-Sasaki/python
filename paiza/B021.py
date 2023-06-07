N = int(input())
for _ in range(N):
    a = input()
    if a[-1] == "s" or a[-1] == "o" or a[-1] == "x" or a[-2:] == "sh" or a[-2:] == "ch":
        a += "es"
    elif a[-1] == "f":
        a = a[:-1] + "ves"
    elif a[-2:] == "fe":
        a = a[:-2] + "ves"
    elif a[-1] == "y":
        if a[-2] != "a" and a[-2] != "i" and a[-2] != "u" and a[-2] != "e" and a[-2] != "o":
            a = a[:-1] + "ies"
        else:
            a += "s"
    else:
        a += "s"
    print(a)
