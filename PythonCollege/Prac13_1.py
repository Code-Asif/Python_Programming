#Python Program to Reverse a String using Recursion.

def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

str = input("Enter a string: ")
print("Reversed string:")
print(reverse(str))