#Python program to check whether a string is palindrome or not
str = input("Enter a word: ")
str1 = str[::-1]
if str == str1:
    print("Palindrome")
else:
    print("Not palindrome")