#Python program to insert a number to any position in a list.
n = int(input("Enter size: "))
list = []
for i in range(n):
    list.append(int(input("Enter num: ")))

pos = int(input("Enter position to insert element: "))
ele = int(input("Enter element to enter: "))
list.insert(pos, ele)
print(list)