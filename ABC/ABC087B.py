arr = list(input() for i in range(4))
#[input() for i in range(4)]としても可能
count = 0
sum = 0
for fihun in range(int(arr[0]) + 1):
    for hun in range(int(arr[1]) + 1):
        for fi in range(int(arr[2]) + 1):
            sum = fihun * 500 + hun * 100 + fi * 50
            if sum == int(arr[3]):
                count += 1
print(count)
