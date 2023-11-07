#Python program to find the product of a set of real numbers.

a = int(input("Enter how many: "))
pro = 1
for i in range(1,a+1,1):
    pro *= i
print(pro)
