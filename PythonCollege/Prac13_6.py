#Python Program to Check if a Given String is Palindrome.

def isPalindrome(str, n):
    j= n-1
    str2 = ""
    for i in range(n):
        str2 += str[j]
        j -= 1
    if str2 == str:
        print("String is palindrome")
    else:
        print("String is not palindrome")

str = input("Enter a string: ")
isPalindrome(str, len(str))
