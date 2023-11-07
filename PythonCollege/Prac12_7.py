#Python Program to Remove Odd Indexed Characters in a string.

def removeOddIndex(str):
    newStr = ""
    for i in range(len(str)):
        if i%2 == 0:
            newStr += str[i]
    return newStr

str = input("Enter a string: ")
print("String after removing odd indexed characters:")
print(removeOddIndex(str))
