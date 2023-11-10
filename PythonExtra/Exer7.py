# Renaming all files in a perticular folder ends with .png
import os

files = os.listdir("book_data")

i = 1
for file in files:
    if file.endswith(".txt"):
        print(f"{file}")
        os.rename(f"./book_data/{file}", f"./book_data/{i}.txt")
        i = i + 1
