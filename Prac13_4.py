#Python Program to Count Number of Uppercase and Lowercase Letters in a String

def countUpperLower(str):
    countUpper = 0
    countLower = 0
    for i in str:
        if i.isupper():
            countUpper += 1
        elif i.islower():
            countLower += 1
    return countUpper, countLower

str = input("Enter a string: ")
countUpper, countLower = countUpperLower(str)
print("Number of uppercase characters in the string:")
print(countUpper)
print("Number of lowercase characters in the string:")
print(countLower)