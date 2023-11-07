#Python Program to Find Largest Number in a List

def max(list, n):
    max = list[0]
    for i in range(n):
        if max < list[i]:
            max = list[i]
    return max

list = []
n = int(input("Enter number of element: "))
for i in range(n):
    list.append(int(input("Enter element: ")))

print("Max: ", max(list,n))
