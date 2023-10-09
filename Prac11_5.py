#Python program to delete an element from a list by index.
n = int(input("Enter size of list: "))
list = []

for i in range(n):
    list.append(int(input("Enter element to insert: ")))

pos = int(input("Enter position: "))
list.pop(pos)
print(list)