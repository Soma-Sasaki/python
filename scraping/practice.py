import os, glob
path = r"C:\Users\shira\Desktop\ぱわぽ"
files = glob.glob("s-sasaki*")
print(files)
for file in files:
    temp = os.path.join(path, file)
    print(temp)
    temp2 = temp.replace("s-sasaki_","")
    print(temp2)
    os.rename(temp, temp2)
