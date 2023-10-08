#Python program to find the sum of the digits of an integer using while loop.

num = int(input("Enter num: "))
temp = num
sum=0
while num!=0:
    digit = num%10
    sum += digit
    num//=10
    
print("Sum of digit of ",temp," is :",sum )
