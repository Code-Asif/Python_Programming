#Python program to display the sum of n numbers using a list.
list = []
sum = 0
n = int(input("Enter the number of elements: "))
for i in range(n):
    list.append(int(input("Enter a number: ")))
for i in range(n):
    sum = sum + list[i]
print("Sum of the numbers is ",sum)