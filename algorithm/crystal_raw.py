def HowHardIsTheCrystal(n, d):
    r = 1
    while (r**d <= n):
        r = r + 1
    print("Radix chosen is {}".format(r))
    numDrops = 0
    floorNoBreak = [0] * d
    for i in range(d):
        for j in range(r-1):
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r, d, floorNoBreak)
            if Floor > n:
                print(floorNoBreak)
                floorNoBreak[i] -= 1
                break

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d):
        number += rep[i] * (r**(d-i-1))
    return number

HowHardIsTheCrystal(128, 4)
