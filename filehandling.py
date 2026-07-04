#create and write file
file = open("filehandling.txt", "w")
file.write("\nMy name is Ganesh.")

file.write("\nI am studying MCA second year.")

file.write("\nI am learning Python programming.")

file.write("\nPython is easy and powerful.")

file.write("\nI want to become a software developer.")

file.close()


# read the content of the file 
with open("filehandling.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("total lines:", len(words))

# print top 2 line only from  the file
with open("filehandling.txt", "r") as f:
    for i in range(3):
        line = f.readline()
        print(line.strip())

# file removing 
import os
if os.path.exists("filehandli.txt"):
    os.remove("filehandli.txt")
    print("file removed successfully")
else:
    print("file does not exist")

# in the file one string is here i want to count that string using file handling


