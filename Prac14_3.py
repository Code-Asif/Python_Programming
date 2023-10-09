#Python Program to Swap the First and Last Element in a List.

def swapFirstLast(list):
    if len(list) == 1:
        return list
    else:
        return [list[-1]] + list[1:-1] + [list[0]]
    
list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input("Enter element: ")))
    
print("List after swapping first and last elements:")
print(swapFirstLast(list))
