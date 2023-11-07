#Python program to display the given integer in reverse manner.

num = int(input("Enter a number: "))
rev=0
digit=0
while num != 0:
    digit = num%10
    rev = rev*10+digit
    num //= 10
print("Reverse : ", rev)
