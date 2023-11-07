# Python program to find the odd numbers in an array
n = int(input("Enter size of array: "))
list = []

for i in range(n):
    list.append(int(input("Enter n: ")))

for i in range(n):
    if(list[i]%2 !=0):
        print(list[i], end="\t")
