#Python Program that inputs a text file. The program should print all of the unique words in the file in alphabetical order

def printDict(dict):
    for i in dict:
        print(i, ":", dict[i])

def main():
    file = open("file.txt", "r")
    dict = {}
    for line in file:
        for word in line.split():
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    printDict(dict)
    file.close()

main()