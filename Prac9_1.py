#Python program to check whether the given integer is a multiple of both 5 and 7

a = int(input("Enter a number: "))
if (a%5==0 and a%7==0) :
    print(a,"is divisible by both 5 and 7")
elif(a%5==0):
    print(a,"is divisible by 5 only")
elif(a%7==0):
    print(a,"is divisibly by 7 only")
else:
    print(a,"is not divisible by 5 or 7")
