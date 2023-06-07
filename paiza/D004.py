s = int(input())
print("Hello ", end="")
for i in range(s - 1):
    ns = input()
    print(ns + ",", end="")
ns = input()
print(ns + ".")
