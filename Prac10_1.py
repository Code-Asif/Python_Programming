#Python program to check whether the given integer is a prime number or not.

num = int(input("Enter a number: "))
count=0
for i in range(2, num):
    if(num%i==0):
        count+=1
if count==0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")