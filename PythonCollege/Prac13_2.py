#Python Program to Reverse a String Without using Recursion.

def rev(str, n):
    j= n-1
    str2 = ""
    for i in range(n):
        str2 += str[j]
        j -= 1
    return str2
    

str = input("Enter a string: ")
print("Reversed string:", rev(str, len(str)))