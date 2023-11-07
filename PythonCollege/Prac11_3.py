#Python program to find the largest number in a list without using built-in functions.

n = int(input("Enter size of list: "))
list = []
for i in range(n):
    list.append(int(input("Enter n: ")))

max = list[0]
for i in range(n):
    if max < list[i]:
        max = list[i]

print("Max: ",max)