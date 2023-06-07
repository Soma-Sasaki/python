import time

for i in range(10):
    time.sleep(1)
    if (i+1)%3 == 0:
        print("python最高!")
    else:
        print(f"{i+1}秒経過")
