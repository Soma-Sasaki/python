x=int(input())

a=list(int(2**i) for i in range(10))

if x in a:
    print("OK")
else:
    print("NG")
