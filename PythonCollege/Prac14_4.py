#Python Program to Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file

def copyFile():
    file1 = input("Enter name of first file: ")
    file2 = input("Enter name of second file: ")
    f1 = open(file1, "r")
    f2 = open(file2, "w")
    f2.write(f1.read())
    f1.close()
    f2.close()

copyFile()