#Python Program to Check if a Given String is Palindrome.

def isPalindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True
    else:
        if str[0] == str[-1]:
            return isPalindrome(str[1:-1])
        else:
            return False

str = input("Enter a string: ")
if isPalindrome(str):
    print("String is palindrome")
else:
    print("String is not palindrome")
