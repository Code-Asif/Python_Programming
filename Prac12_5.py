#Python program to print all the items in a dictionary.

def printDict(dict):
    for i in dict:
        print(i, ":", dict[i])

dict = {'Name': 'Asif', 'Age': 21, 'Class': 'EC1'}
printDict(dict)
