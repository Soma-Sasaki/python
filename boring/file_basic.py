import os, shelve

os.chdir(r"C:\Users\shira\Desktop\python\boring")
hello_file = open("hello.txt", "w")
hello_file.write("Helloooooo!!!!!")
hello_file.close()

bacon_file = open("bacon.txt", "w")
bacon_file.write("Hello world!\n")
bacon_file.close()

bacon_file = open("bacon.txt", "a")
bacon_file.write("bacon is not a vegetable.")
bacon_file.close()

shelf_file = shelve.open("mydata")
cats = ["Zophie", "Pooka", "Simon"]
shelf_file["cats"] = cats
shelf_file.close()

shelf_file = shelve.open("mydata")


birthday_file = open("07-03-1998.txt", "w")
birthday_file.write("Happy Birthday!\n")
birthday_file.close()
