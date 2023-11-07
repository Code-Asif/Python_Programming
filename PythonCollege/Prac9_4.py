#Python program to find the geometric mean of n numbers
import math
num = int(input("Enter n: "))
prod=1
for i in range(1, num+1):
    prod *=i
print(math.sqrt(prod))
