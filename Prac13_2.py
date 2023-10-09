#Python Program to Reverse a String Without using Recursion.

def reverse(str):
    newStr = ""
    for i in range(len(str)-1,-1,-1):
        newStr += str[i]
    return newStr

str = input("Enter a string: ")
print("Reversed string:")
print(reverse(str))