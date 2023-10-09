#Python Program to Find Largest Number in a List

def findLargest(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], findLargest(list[1:]))
    
list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input("Enter element: ")))
    
print("Largest number in the list:")
print(findLargest(list))
