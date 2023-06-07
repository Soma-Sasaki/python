import shutil, os
import send2trash
import zipfile

os.chdir(r"C:\Users\shira\Desktop\python\boring")
shutil.copy(r".\bacon.txt", r"..\algorithm")
send2trash.send2trash(r"..\algorithm\bacon.txt")

#ディレクトリツリーを渡り歩く
for foldername, subfolders, filenames in os.walk(r"../"):
    print("The current folder is " + foldername)
    for subfolder in subfolders:
        print("SUBFOLDER OF " + foldername + ": " + subfolder)
    for filename in filenames:
        print("FILE INSIDE " + foldername + ": " + filename)
    print("")

#ZIP
new_zip = zipfile.ZipFile("new.zip", "w")
new_zip.write("bacon.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
