#Python Program to Count Number of Lowercase Characters in a String.

def countLower(str):
    count = 0
    for i in str:
        if i.islower():
            count += 1
    return count

str = input("Enter a string: ")
print("Number of lowercase characters in the string:")
print(countLower(str))